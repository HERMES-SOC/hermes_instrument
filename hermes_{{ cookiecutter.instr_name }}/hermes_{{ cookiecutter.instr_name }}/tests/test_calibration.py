import pytest
import os.path
from pathlib import Path

import numpy as np
from numpy.random import random
from astropy.timeseries import TimeSeries
from astropy.units import Quantity
import astropy.units as u
from astropy.nddata import NDData
from astropy.wcs import WCS
from ndcube import NDCube, NDCollection
from spacepy.pycdf import CDFError

from hermes_core.timedata import HermesData
from hermes_core.util.util import create_science_filename, parse_science_filename
import hermes_{{ cookiecutter.instr_name }}.calibration as calib

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

    # Spectra Data
    spectra = NDCollection(
        [
            (
                "test_spectra",
                NDCube(
                    data=random(size=(4, 10)),
                    wcs=WCS(naxis=2),
                    meta={"CATDESC": "Test Spectra Variable"},
                    unit="eV",
                ),
            )
        ]
    )

    # Global Metadata Attributes
    input_attrs = HermesData.global_attribute_template("instrument", "l1", "1.0.0")

    # Create HermesData Object
    hermes_data = HermesData(
        timeseries=ts, support=support, spectra=spectra, meta=input_attrs
    )
    hermes_data.timeseries["Bx"].meta.update({"CATDESC": "Test"})
    return hermes_data


def test_process_file_nofile_error():
    """
    Test that if file does not exist it produces the correct error.
    The file needs to be in the correct format.
    """
    with pytest.raises(FileNotFoundError):
        calib.process_file(Path("hermes_instrument_l0_2032339-000000_v0.bin"))


def test_calibrate_data():
    test_data = get_test_hermes_data()

    with pytest.raises(ValueError) as excinfo:
        calib.calibrate_data(test_data)
    assert (
        str(excinfo.value)
        == "Calibration file for hermes_instrument_l1_20160322T123031_v1.0.0 not found."
    )


def test_process_file_level0(level0_file):
    with pytest.raises(FileNotFoundError) as excinfo:
        _ = calib.process_file(level0_file)


def test_process_file_level1(level1_file):
    with pytest.raises(CDFError) as excinfo:
        _ = calib.process_file(level1_file)
    assert str(excinfo.value) == "CDF_READ_ERROR: Read failed - error from file system."


def test_get_calibration_file():
    assert calib.get_calibration_file("") is None
