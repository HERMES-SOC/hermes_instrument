import pytest
from hermes_instrument.calibration.calibration import *


def test_calibrate_file():
    with pytest.raises(ValueError) as excinfo:
        calibrate_file("datafile_with_no_calib.cdf")
    assert (
        str(excinfo.value)
        == "Calibration file for datafile_with_no_calib.cdf not found."
    )


def test_get_calibration_file():
    assert get_calibration_file("") is None


def test_read_calibration_file():
    assert read_calibration_file("calib_file") is None
