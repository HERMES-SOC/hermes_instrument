import pytest
from pathlib import Path

from hermes_{{ cookiecutter.instr_name }}.io.file_tools import load_data_file, read_calibration_file, write_data_file

level0_filename = "hermes_instrument_l0_2022339-000000_v0.bin"
level1_filename = "hermes_instrument_l1_20221205T000000_v1.0.0.cdf"
ql_filename = "hermes_instrument_ql_20221205T000000_v1.0.0.cdf"


@pytest.fixture(scope="session")
def level0_file(tmp_path_factory):
    fn = tmp_path_factory.mktemp("data") / level0_filename
    with open(fn, "w"):
        pass
    return fn


@pytest.fixture(scope="session")
def level1_file(tmp_path_factory):
    fn = tmp_path_factory.mktemp("data") / level1_filename
    with open(fn, "w"):
        pass
    return fn


def test_load_data_file(level0_file):
    with pytest.raises(FileNotFoundError) as excinfo:
        _ = load_data_file(level0_file)


def test_read_calibration_file():
    assert read_calibration_file("calib_file") is None
