import glob


def pytest_addoption(parser):
    parser.addoption(
        "--filename",
        action="store",
        type=str,
        help="list of files to pass to test functions",
    )
    parser.addoption("--cv", action="store", default="default name")


def pytest_generate_tests(metafunc):
    if "filename" in metafunc.fixturenames:
        metafunc.parametrize(
            "filename", glob.glob(str(metafunc.config.getoption("filename")))
        )
