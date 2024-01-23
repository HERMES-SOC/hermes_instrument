"""
A module for all things calibration.
"""
import random
from pathlib import Path

import astropy

from hermes_core.timedata import HermesData

from hermes_{{ cookiecutter.instr_name }} import log
import hermes_{{ cookiecutter.instr_name }}
from hermes_{{ cookiecutter.instr_name }}.io import load_data_file, read_calibration_file, write_data_file

__all__ = [
    "process_file",
    "calibrate_data",
    "get_calibration_file",
]


def process_file(data_filename: Path) -> list:
    """
    This is the entry point for the pipeline processing.
    It runs all of the various processing steps required.

    Parameters
    ----------
    data_filename: str
        Fully specificied filename of an input file

    Returns
    -------
    output_filenames: list[str]
        Fully specificied filenames for the output files.
    """
    log.info(f"Processing file {data_filename}.")
    output_files = []

    # Load the data file to a logical data format from its physical file format
    instrument_data = load_data_file(data_filename)

    # Calibrate the data file in its logical data format
    calibrated_data = calibrate_data(instrument_data)

    # Write the logical data format to a physical file format
    output_path = data_filename.partent
    calibrated_filename = write_data_file(calibrated_data, output_path=output_path)

    # Add the calibrated filename to the list of returned files to the processing pipeline
    output_files.append(calibrated_filename)
    #  data_plot_files = plot_file(data_filename)
    #  calib_plot_files = plot_file(calibrated_file)

    # add other tasks below
    return output_files


def calibrate_data(instrument_data: HermesData) -> HermesData:
    """
    Given a data conainer with uncalibrated data from an input file, calibrate the data
    and and return a data container of the calibrated data.

    Function should calibrate and increase the data level by one-level. For example,
    if the data container `instrument_data` contains L0 data, calibrate the data to L1
    data. If the the `instrument_data` contains L1 data, calibrate the data to L2 data.

    Calibrating from L0 -> L4 data requres multiple successive calls to the `calibrate_data`
    function.
    
    Parameters
    ----------
    instrument_data: HermesData
        A data container in a logical data format from a non-calibrated file (data level < 2)

    Returns
    -------
    output_data: HermesData
        A data container in a logical data format to create a calibrated file

    Examples
    --------
    """

    # example log messages
    log.info("Despiking removing {num_spikes} spikes".format(num_spikes=random.randint(0, 10)))
    log.warning("Despiking could not remove {num_spikes}".format(num_spikes=random.randint(1, 5)))

    # Example loading a calibration file
    calib_file = get_calibration_file(instrument_data)
    if calib_file is None:
        raise ValueError(
            "Calibration file for {} not found.".format(instrument_data.meta["Logical_file_id"])
        )
    else:
        calib_data = read_calibration_file(calib_file)

    # Create output data
    output_data = instrument_data  # NOTE : Template does not modify input data

    return output_data


def get_calibration_file(instrument_data: HermesData, time: astropy.time.Time = None) -> Path:
    """
    Given a time, return the appropriate calibration file.

    Parameters
    ----------
    instrument_data: HermesData
        A data container in a logical data format
    time: ~astropy.time.Time

    Returns
    -------
    calib_filename: Path
        Fully specificied filename for the appropriate calibration file.

    Examples
    --------
    """
    return None
