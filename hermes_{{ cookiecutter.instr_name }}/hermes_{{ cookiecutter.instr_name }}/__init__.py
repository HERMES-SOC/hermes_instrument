# Licensed under Apache License v2 - see LICENSE.rst
import os.path

from hermes_core import log

try:
    from ._version import version as __version__
    from ._version import version_tuple
except ImportError:
    __version__ = "unknown version"
    version_tuple = (0, 0, "unknown version")

__all__ = ["log"]

_package_directory = os.path.dirname(os.path.abspath(__file__))
_data_directory = os.path.abspath(os.path.join(_package_directory, "data"))

log.debug(f"hermes_{{ cookiecutter.instr_name }} version: {__version__}")
