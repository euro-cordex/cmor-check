from ..cmor_check import cmor_check
from ..datasets import CORDEX_CMIP6_DS
from ..tables import CORDEX_CMIP6_TABLE

mpi_esm_hr_url = "https://esgf3.dkrz.de/thredds/fileServer/cmip6/CMIP/MPI-M/MPI-ESM1-2-LR/historical/r1i1p1f1/Amon/tas/gn/v20190710/tas_Amon_MPI-ESM1-2-LR_historical_r1i1p1f1_gn_185001-186912.nc"
ec_earth_veg_url = "https://esg-dn1.nsc.liu.se/thredds/fileServer/esg_dataroot6/cmip6data/CMIP6/CMIP/EC-Earth-Consortium/EC-Earth3-Veg/historical/r1i1p1f1/Amon/tas/gr/v20211207/tas_Amon_EC-Earth3-Veg_historical_r1i1p1f1_gr_185001-185012.nc"
cordex_url = "https://raw.githubusercontent.com/euro-cordex/py-cordex-data/main/CORDEX/CMIP6/DD/EUR-12/GERICS/ERA5/evaluation/r1i1p1f1/REMO2020/v1/fx/orog/v20240529/orog_EUR-12_ERA5_evaluation_r1i1p1f1_GERICS_REMO2020_v1_fx.nc"


def test_cmor():
    ds = CORDEX_CMIP6_DS
    cv = CORDEX_CMIP6_TABLE("CV")
    return cmor_check(ds, cv)
