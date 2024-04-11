import pytest

from ..cmor_check import check_file

# @pytest.fixture(scope="session")
# def filenames(pytestconfig):
#     filenames = pytestconfig.getoption("filenames")
#     if isinstance(filename, list):
#         return filenames
#     if "*" in filenames:
#         return sorted(glob.glob(filenames))


@pytest.fixture(scope="session")
def cv(pytestconfig):
    return pytestconfig.getoption("cv")


def test_cmor(filename, cv):
    return check_file(filename, cv)
