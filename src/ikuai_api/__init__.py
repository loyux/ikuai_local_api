from importlib.metadata import version, PackageNotFoundError
try:
    __version__ = version("ikuai_local_api")
except PackageNotFoundError:
    __version__ = "unknown version"

from ikuai_api.cli import cli
from ikuai_api.ikuai import Router