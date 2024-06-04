url = "https://raw.githubusercontent.com/euro-cordex/py-cordex-data/main/CORDEX/CMIP6/DD/EUR-12/GERICS/ERA5/evaluation/r1i1p1f1/REMO2020/v1/fx/orog/v20240529/orog_EUR-12_ERA5_evaluation_r1i1p1f1_GERICS_REMO2020_v1_fx.nc"


def _cordex_cmip6():
    import cordex as cx

    ds = cx.cordex_domain("EUR-11", mip_era="CMIP6", dummy="tas", bounds=True)
    ds.tas.attrs = {
        "standard_name": "air_temperature",
        "long_name": "Near-Surface Air Temperature",
        "units": "K",
        "cell_methods": "area: time: mean",
        "cell_measures": "area: areacella",
        "history": "2024-05-29T19:45:00Z altered by CMOR: Treated scalar dimension: 'height'.",
        "grid_mapping": "rotated_latitude_longitude",
    }
    ds.attrs = {
        "Conventions": "CF-1.11",
        "activity_id": "DD",
        "contact": "gerics-cordex@hereon.de",
        "creation_date": "2024-05-29T19:45:00Z",
        "domain": "Europe",
        "domain_id": "EUR-12",
        "driving_experiment": "reanalysis simulation of the recent past",
        "driving_experiment_id": "evaluation",
        "driving_institution_id": "ECMWF",
        "driving_source_id": "ERA5",
        "driving_variant_label": "r1i1p1f1",
        "experiment_id": "evaluation",
        "external_variables": "areacella",
        "frequency": "mon",
        "grid": "Rotated-pole latitude-longitude with 0.11 degree grid spacing",
        "history": "2024-05-29T19:45:00Z ;rewrote data to be consistent with CORDEX for variable tas found in table mon.",
        "institution": "Climate Service Center Germany, Helmholtz Centre hereon GmbH, Hamburg, Germany",
        "institution_id": "GERICS",
        "label": "REMO2020",
        "mip_era": "CMIP6",
        "product": "model-output",
        "project_id": "CORDEX",
        "realm": "REALM",
        "references": "https://www.remo-rcm.de",
        "run_variant": "1st realization",
        "source": "REMO regional model (2022)",
        "source_id": "REMO2020",
        "source_type": "ARCM",
        "table_id": "mon",
        "table_info": "Creation Date:(05 April 2024) MD5:48d6a0d158eeac713bdad57279c1277d",
        "title": "REMO2020 output prepared for CMIP6",
        "tracking_id": "hdl:21.14103/a01f9b6f-09d0-4680-a656-63f66ce3828a",
        "variable_id": "tas",
        "version_realization": "v1",
        "license": "https://cordex.org/data-access/cordex-cmip6-data/cordex-cmip6-terms-of-use",
        "cmor_version": "3.8.0",
    }
    return ds

CORDEX_CMIP6_DS = _cordex_cmip6()
