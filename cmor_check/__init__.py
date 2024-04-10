import pkg_resources

from .cmor_check import cmor_check

try:
    __version__ = pkg_resources.get_distribution("py-cordex").version
except Exception:
    # Local copy or not installed with setuptools.
    # Disable minimum version checks on downstream libraries.
    __version__ = "999"

__all__ = ["cmor_check"]
