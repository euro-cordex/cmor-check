# cmor-check

:construction: UNDER CONSTRUCTION, USE WITH CARE

[![github CI](https://github.com/euro-cordex/cmor-check/actions/workflows/ci.yaml/badge.svg)](https://github.com/euro-cordex/cmor-check/actions/workflows/ci.yaml)

tools to check cmorized data

## API

Use the API to integrate seamlessly into your workflows:

```python
from cmor_check import cmor_check
from cmor_check.datasets import CORDEX_CMIP6_DS
from cmor_check.tables import CORDEX_CMIP6_TABLE

CORDEX_CMIP6_DS
```
![grafik](https://github.com/euro-cordex/cmor-check/assets/5659125/eb05d8de-6988-4b43-a807-8b73b1482d02)

running `cmor_check` on the example dataset:
```python
cmor_check(CORDEX_CMIP6_DS, CORDEX_CMIP6_TABLE("CV"))
```

gives

```bash
INFO - Found project_id: CORDEX (cmor_check.py:56)
INFO - Checking CV (cmor_check.py:68)
INFO - required global attributes: ['activity_id', 'contact', 'Conventions', 'creation_date', 'domain_id', 'domain', 'driving_experiment_id', 'driving_experiment', 'driving_institution_id', 'driving_source_id', 'driving_variant_label', 'frequency', 'grid', 'institution', 'institution_id', 'license', 'mip_era', 'product', 'project_id', 'source', 'source_id', 'source_type', 'tracking_id', 'variable_id', 'version_realization'] (cmor_check.py:13)
INFO - Found value 'DD' for required global attribute 'activity_id' (cmor_check.py:29)
INFO - Found value 'CF-1.11' for required global attribute 'Conventions' (cmor_check.py:29)
INFO - Found value 'EUR-12' for required global attribute 'domain_id' (cmor_check.py:29)
INFO - Found value 'evaluation' for required global attribute 'driving_experiment_id' (cmor_check.py:29)
INFO - Found value 'ERA5' for required global attribute 'driving_source_id' (cmor_check.py:29)
INFO - Found value 'mon' for required global attribute 'frequency' (cmor_check.py:29)
INFO - Found value 'GERICS' for required global attribute 'institution_id' (cmor_check.py:29)
INFO - Found value 'https://cordex.org/data-access/cordex-cmip6-data/cordex-cmip6-terms-of-use' for required global attribute 'license' (cmor_check.py:29)
INFO - Found value 'CMIP6' for required global attribute 'mip_era' (cmor_check.py:29)
INFO - Found value 'model-output' for required global attribute 'product' (cmor_check.py:29)
INFO - Found value 'CORDEX' for required global attribute 'project_id' (cmor_check.py:29)
INFO - Found value 'REMO2020' for required global attribute 'source_id' (cmor_check.py:29)
INFO - Found value 'ARCM' for required global attribute 'source_type' (cmor_check.py:29)
WARNING - value 'hdl:21.14103/a01f9b6f-09d0-4680-a656-63f66ce3828a' of required global attribute 'tracking_id' is not one of ['hdl:21.14103/.*']. (cmor_check.py:26)
INFO - Found domain_id: EUR-12 (cmor_check.py:46)
INFO - Checking coordinate: rlon (cmor_check.py:35)
INFO - Checking coordinate: rlat (cmor_check.py:35)
```

## Command line tool

For quick checks of files, use the command line tool:

```bash
cmor-check --help
```

gives

```bash
Usage: cmor-check [OPTIONS] FILENAME

Options:
  --cv TEXT  path to CV table
  --help     Show this message and exit.
```
For example:
```bash
curl  -O -J https://raw.githubusercontent.com/euro-cordex/py-cordex-data/main/CORDEX/CMIP6/DD/EUR-12/GERICS/ERA5/evaluation/r1i1p1f1/REMO2020/v1/fx/orog/v20240529/orog_EUR-12_ERA5_evaluation_r1i1p1f1_GERICS_REMO2020_v1_fx.nc
curl -O -J https://raw.githubusercontent.com/WCRP-CORDEX/cordex-cmip6-cmor-tables/main/Tables/CORDEX-CMIP6_CV.json

cmor-check --cv CORDEX-CMIP6_CV.json orog_EUR-12_ERA5_evaluation_r1i1p1f1_GERICS_REMO2020_v1_fx.nc
````
gives the same results as above.
