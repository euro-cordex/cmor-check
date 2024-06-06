from compliance_checker.base import BaseNCCheck, BaseCheck
from . import __version__


class CMORBaseCheck(BaseCheck):
    _cc_spec_version = __version__
    _cc_spec = "cmor"
    _cc_checker_version = __version__
    _cc_url = "https://github.com/euro-cordex/cmor-check"
    _cc_display_headers = {3: "Required", 2: "Recommended", 1: "Suggested"}


class CMOR_1_Check(BaseNCCheck, CMORBaseCheck):
    _cc_description = "Cmor Check"
    register_checker = True
