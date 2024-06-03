from os import path as op

from .utils import read_json

CORDEX_CMIP6_URL = "https://raw.githubusercontent.com/WCRP-CORDEX/cordex-cmip6-cmor-tables/main/Tables/"


def retrieve(url):
    import pooch

    # URL to one of Pooch's test files
    filename = pooch.retrieve(
        url=url,
        known_hash=None,
        path="~/.cmor-check",
    )
    return filename


def CORDEX_CMIP6(table_id):
    filename = retrieve(op.join(CORDEX_CMIP6_URL, f"CORDEX-CMIP6_{table_id}.json"))
    return read_json(filename)
