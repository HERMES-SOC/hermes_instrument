import pytest
from pathlib import Path
import tempfile

import numpy as np
from numpy.random import random
from astropy.timeseries import TimeSeries
from astropy.units import Quantity
import astropy.units as u
from astropy.nddata import NDData
from spacepy.pycdf import CDFError
import tempfile

from hermes_core.timedata import HermesData
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


def get_test_hermes_data():
    """
    Function to get test hermes_core.timedata.HermesData objects to re-use in other tests
    """

    # Astropy TimeSeries
    ts = TimeSeries(
        time_start="2016-03-22T12:30:31",
        time_delta=3 * u.s,
        data={"Bx": Quantity([1, 2, 3, 4], "gauss", dtype=np.uint16)},
    )

    # Support Data / Non-Time Varying Data
    support = {"support_counts": NDData(data=[1])}

    # Global Metadata Attributes
    input_attrs = HermesData.global_attribute_template("eea", "l1", "1.0.0")

    # Create HermesData Object
    hermes_data = HermesData(timeseries=ts, support=support, meta=input_attrs)
    hermes_data.timeseries["Bx"].meta.update({"CATDESC": "Test"})
    return hermes_data


@pytest.fixture(scope="session")
def level1_file(tmp_path_factory):
    fn = tmp_path_factory.mktemp("data") / level1_filename
    with open(fn, "w"):
        pass
    return fn


def test_load_data_file(level0_file):
    with pytest.raises(RuntimeError) as excinfo:
        _ = load_data_file(level0_file)


def test_read_calibration_file():
    assert read_calibration_file("calib_file") is None

def test_write_data_file():
    test_data = get_test_hermes_data()

    with tempfile.TemporaryDirectory() as tmpdirname:
        test_file_output_path = write_data_file(test_data, output_path=tmpdirname)

        test_file_cache_path = Path(test_file_output_path)
        # Test the File Exists
        assert test_file_cache_path.exists()
