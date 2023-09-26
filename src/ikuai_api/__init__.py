from importlib.metadata import version, PackageNotFoundError
try:
    __version__ = version("ikuai_local_api")
except PackageNotFoundError:
    __version__ = "unknown version"
