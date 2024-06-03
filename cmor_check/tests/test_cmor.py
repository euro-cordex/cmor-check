
from ..cmor_check import cmor_check
from ..datasets import cordex_cmip6


url = "https://raw.githubusercontent.com/euro-cordex/py-cordex-data/main/CORDEX/CMIP6/DD/EUR-12/GERICS/ERA5/evaluation/r1i1p1f1/REMO2020/v1/fx/orog/v20240529/orog_EUR-12_ERA5_evaluation_r1i1p1f1_GERICS_REMO2020_v1_fx.nc"


def test_cmor(filename, cv):
    ds = cordex_cmip6()
    cv = tables.CORDEX_CMIP6("CV")
    checked = cmor_check(ds, cv)
