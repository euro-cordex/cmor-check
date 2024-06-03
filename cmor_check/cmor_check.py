import xarray as xr

from . import log
from .log import get_logger
from .utils import read_json
import numpy as np

logger = get_logger(__name__)


def check_cv(ds, cv_table):
    report = {}
    required_global_attributes = cv_table["required_global_attributes"]
    logger.info(f"required global attributes: {required_global_attributes}")

    for attr in required_global_attributes:
        value = ds.attrs.get(attr)
        if not value:
            logger.error(f"missing required global attribute: {attr}")
            report[attr] = "MISSING"
        elif attr in cv_table.keys():
            cv_values = cv_table[attr]
            if isinstance(cv_values, dict):
                cv_values = list(cv_values.keys())
            if value not in cv_values:
                message = f"value {value} of required global attribute {attr} is not in CV: {cv_values}"
                logger.warning(message)
                report[attr] = message

    return report


def _check_coord(coord, ref):
    logger.info(f"Checking coordinate: {coord.name}")
    close = np.allclose(coord, ref)
    if not close:
        logger.warning(f"Coordinate {coord.name} has wrong values!")
    return close


def check_cordex_grid(ds):
    import cordex as cx
    
    domain_id = ds.cx.domain_id
    logger.info(f"Found domain_id: {domain_id}")
    dm = cx.cordex_domain(domain_id, mip_era="CMIP6", bounds=True)
    
    for axis in ['X', 'Y']:
        _check_coord(ds.cf[axis], dm.cf[axis])    

   
def check_project(ds):
    if "project_id" in ds.attrs:
        project_id = ds.attrs["project_id"]
        logger.info(f"Found project_id: {project_id}")
        return "CORDEX-CMIP6"
    if "activity_id" in ds.attrs:
        logger.info(f"Found activity_id: {activity_id}")
        return "CMIP6"


def cmor_check(ds, cv_table=None, project=None):
    if project is None:
        project = check_project(ds)
    if cv_table:
        logger.info("Checking CV")
        report = check_cv(ds, cv_table.get("CV") or cv_table)
    if project == "CORDEX-CMIP6":
        check_cordex_grid(ds)
    pass


def check_file(filename, cv_table=None):
    ds = xr.open_dataset(filename)
    if cv_table:
        cv_table = read_json(cv_table)
    cmor_check(ds, cv_table)
