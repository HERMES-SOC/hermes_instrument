"""
A module for all things calibration.
"""
import random
from hermes_core import log

__all__ = ["calibrate_file", "get_calibration_file", "read_calibration_file"]


def calibrate_file(data_filename, output_level=2):
    """
    Given an input file, calibrate it and return a new file.

    Parameters
    ----------
    data_filename: str
        Fully specificied filename of the non-calibrated file (data level < 2)
    output_level: int
        The requested data level of the output file.

    Returns
    -------
    output_filename: str
        Fully specificied filename of the non-calibrated file (data level < 2)

    Examples
    --------
    """

    calib_file = get_calibration_file(data_filename)
    if calib_file is None:
        raise ValueError("Calibration file for {} not found.".format(data_filename))
    else:
        calib_data = read_calibration_file(calib_file)

    # example log messages
    log.info(
        "Despiking removing {num_spikes} spikes".format(
            num_spikes=random.randint(0, 10)
        )
    )
    log.warning(
        "Despiking could not remove {num_spikes}".format(
            num_spikes=random.randint(1, 5)
        )
    )

    return None


def get_calibration_file(data_filename, time=None):
    """
    Given a time, return the appropriate calibration file.

    Parameters
    ----------
    data_filename: str
        Fully specificied filename of the non-calibrated file (data level < 2)
    time: ~astropy.time.Time

    Returns
    -------
    calib_filename: str
        Fully specificied filename for the appropriate calibration file.

    Examples
    --------
    """
    return None


def read_calibration_file(calib_filename):
    """
    Given a calibration, return the calibration structure.

    Parameters
    ----------
    calib_filename: str
        Fully specificied filename of the non-calibrated file (data level < 2)

    Returns
    -------
    output_filename: str
        Fully specificied filename of the appropriate calibration file.

    Examples
    --------
    """

    # if can't read the file

    return None
