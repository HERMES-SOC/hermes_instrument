#!/usr/bin/env python
"""
Calibration module unit tests

Parameters
----------
None

Returns
-------
None

Examples
--------
# working directory: /workspaces/hermes_instrument

/usr/bin/python3 -m hermes_instrument.tests.test_calibration

"""
## IMPORT MODULES ##
import pytest
from hermes_instrument.calibration import calibration

## DEFINE FUNCTIONS ##
def test_calibrate_file():
    with pytest.raises(ValueError) as excinfo:
        calibration.calibrate_file("datafile_with_no_calib.cdf")
    assert str(excinfo.value) == "Calibration file for datafile_with_no_calib.cdf not found."


def test_get_calibration_file():
    assert calibration.get_calibration_file("") is None


def test_read_calibration_file():
    assert calibration.read_calibration_file("calib_file") is None


## MAIN PROGRAM ##
if __name__ == "__main__":
    print("Starting unit test: new_cal.py")
    test_calibrate_file()
    test_get_calibration_file()
    test_read_calibration_file()
