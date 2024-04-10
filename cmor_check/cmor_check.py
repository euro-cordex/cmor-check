from . import log
from .log import get_logger
from .utils import read_json

logger = get_logger(__name__)


def check_cv(ds, cv_table):
    report = {}
    required_global_attributes = cv_table["required_global_attributes"]
    logger.info(f"required global attributes: {required_global_attributes}")

    global_attrs = ds.attrs
    for attr in required_global_attributes:
        report[attr] = global_attrs.get(attr) or "ERROR"

    return report


def cmor_check(ds, cv_table=None):
    if cv_table:
        cv_table = read_json(cv_table)
        report = check_cv(ds, cv_table.get("CV") or cv_table)
        for k, v in report.items():
            lev = log.levels[v]
            logger.log(lev, f"{k}: {v}")
    print("cmor check")
