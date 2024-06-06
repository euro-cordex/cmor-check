from compliance_checker.base import BaseNCCheck, BaseCheck, Result
import xarray as xr
from . import __version__
from .tables import CORDEX_CMIP6_TABLE


class CMORBaseCheck(BaseNCCheck):

    _cc_spec_version = __version__
    _cc_spec = "cmor"
    _cc_checker_version = __version__
    _cc_url = "https://github.com/euro-cordex/cmor-check"

    @classmethod
    def make_result(cls, level, score, out_of, name, messages):
        return Result(level, (score, out_of), name, messages)

    def setup(self, ds):
        """
        Set up the checker by assigning the dataset and creating the dict
        of meshes it will need to check through.

        Parameters
        ----------
        ds : netCDF4 dataset object
        """

        self.ds = xr.open_dataset(xr.backends.NetCDF4DataStore(ds))
        self.cv = CORDEX_CMIP6_TABLE("CV").get("CV") or CORDEX_CMIP6_TABLE("CV")


class CMOR_1_Check(CMORBaseCheck):

    _cc_display_headers = {3: "Required", 2: "Recommended", 1: "Suggested"}
    _cc_description = "Cmor Check"
    register_checker = True

    def __init__(self):
        pass

    def check_required_global_attributes(self, ds):
        """
        Check check for mandatory attributes.
        """

        level = BaseCheck.HIGH
        score = 0
        messages = []
        desc = "Check for required global attributes."

        required_attributes = self.cv.get("required_global_attributes", {})

        out_of = len(required_attributes)

        for attr in required_attributes:
            test = attr in self.ds.attrs
            score += int(test)
            if not test:
                messages.append(f"Required global attribute {attr} is missing")

        return self.make_result(level, score, out_of, desc, messages)
