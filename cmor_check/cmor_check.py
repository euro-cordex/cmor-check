import xarray as xr

from . import log
from .log import get_logger
from .utils import read_json

logger = get_logger(__name__)


def check_cv(ds, cv_table):
    report = {}
    required_global_attributes = cv_table["required_global_attributes"]
    logger.info(f"required global attributes: {required_global_attributes}")

    for attr in required_global_attributes:
        report[attr] = ds.attrs.get(attr) or "ERROR"

    return report


def cmor_check(ds, cv_table=None):
    if cv_table:
        logger.info("Checking CV")
        report = check_cv(ds, cv_table.get("CV") or cv_table)
        for k, v in report.items():
            lev = log.levels[v]
            logger.log(lev, f"{k}: {v}")


def check_file(filename, cv_table=None):
    ds = xr.open_dataset(filename)
    if cv_table:
        cv_table = read_json(cv_table)
    cmor_check(ds, cv_table)
