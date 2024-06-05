import numpy as np
from .log import get_logger

logger = get_logger(__name__)


def _check_coord(coord, ref):
    logger.info(f"Checking coordinate: {coord.name}")
    close = np.allclose(coord, ref)
    if not close:
        logger.warning(f"Coordinate {coord.name} has wrong values!")
    return close


def check_cordex_grid(ds):
    """Check dataset coordinates if they are close to official specifications"""
    import cordex as cx

    domain_id = ds.cx.domain_id
    if not domain_id:
        logger.warning("Checking for CORDEX grid but no domain_id found!")
    logger.info(f"Found domain_id: {domain_id}")
    dm = cx.cordex_domain(domain_id, mip_era="CMIP6", bounds=True)

    for axis in ["X", "Y"]:
        _check_coord(ds.cf[axis], dm.cf[axis])
