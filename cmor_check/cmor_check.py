import xarray as xr

from .log import get_logger
from .utils import read_json
from .checks import check_cordex_grid
import re

logger = get_logger(__name__)


def _compare_re(pattern, string):
    """compare two strings or regex"""
    logger.debug(f"pattern: {pattern}, string: {string}")
    return bool(re.fullmatch(pattern, str(string), flags=re.ASCII))


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
            if isinstance(cv_values, list) and len(cv_values) == 1:
                # only one possible outcome or pattern, might be regex
                if not _compare_re(cv_values[0], value):
                    message = f"value '{value}' of required global attribute '{attr}' does not match {cv_values[0]}."
                    logger.error(message)
                    report[attr] = message
                    continue
            elif value not in cv_values:
                message = f"value '{value}' of required global attribute '{attr}' is not one of {cv_values}."
                logger.error(message)
                report[attr] = message
                continue
            # came here, so it checked out
            logger.info(
                f"Checked value '{value}' of required global attribute '{attr}' to be consistent with CV."
            )
        else:
            logger.info(f"Found value '{value}' of required global attribute '{attr}'.")

    return report


def check_project(ds):
    if "project_id" in ds.attrs:
        project_id = ds.attrs["project_id"]
        logger.info(f"Found project_id: {project_id}")
        return "CORDEX-CMIP6"
    if "activity_id" in ds.attrs:
        activity_id = ds.attrs["activity_id"]
        logger.info(f"Found activity_id: {activity_id}")
        return "CMIP6"


def cmor_check(ds, cv_table=None, project=None):
    if project is None:
        project = check_project(ds)
    if cv_table:
        logger.info("Checking CV")
        check_cv(ds, cv_table.get("CV") or cv_table)
    if project == "CORDEX-CMIP6":
        check_cordex_grid(ds)
    pass


def check_file(filename, cv_table=None):
    ds = xr.open_dataset(filename)
    if cv_table:
        cv_table = read_json(cv_table)
    cmor_check(ds, cv_table)
