"""
A module for all things calibration.
"""
import random
from pathlib import Path
import astropy
from hermes_core.timedata import HermesData
from hermes_core.util.validation import validate
from hermes_{{ cookiecutter.instr_name }} import log

__all__ = ["calibrate_file", "get_calibration_file", "read_calibration_file"]

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
    calibrated_filename = write_data_file(calibrated_data)

    # Add the calibrated filename to the list of returned files to the processing pipeline
    output_files.append(calibrated_filename)
    #  data_plot_files = plot_file(data_filename)
    #  calib_plot_files = plot_file(calibrated_file)

    # add other tasks below
    return output_files

def load_data_file(data_filename : Path) -> HermesData:
    """
    Given an input file, load the file's data from a physical file data format
    to a logical data format that can be used for calibration and analysis. 

    Parameters
    ----------
    data_filename: Path
        Fully specificied filename of the input data file.

    Returns
    -------
    instrument_data: HermesData
        A data container in a logical data format for loading, storing, and manipulating 
        HERMES time series data

    Examples
    --------
    """
    
    # As an example, you can load CDF files directly into the data container
    return HermesData.load(data_filename)

def calibrate_data(instrument_data: HermesData, output_level: int = 2) -> HermesData:
    """
    Given an input file, calibrate it and return a new file.

    Parameters
    ----------
    instrument_data: HermesData
        A data container in a logical data format from a non-calibrated file (data level < 2)
    output_level: int
        The requested data level of the output data container.

    Returns
    -------
    output_data: HermesData
        A data container in a logical data format to create a calibrated file

    Examples
    --------
    """
    
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

    # Example loading a calibration file 
    calib_file = get_calibration_file(instrument_data)
    if calib_file is None:
        raise ValueError(
            "Calibration file for {} not found.".format(instrument_data.meta["Logical_file_id"])
        )
    else:
        calib_data = read_calibration_file(calib_file)
        
    # Create output data
    output_data = instrument_data # NOTE : Template does not modify input data

    return output_data

def write_data_file(instrument_data: HermesData) -> str:
    """
    Given an input data container in a logical data format, write the data to 
    a physical file data format.

    Parameters
    ----------
    instrument_data: HermesData
        A data container in a logical data format

    Returns
    -------
    output_filename: str
        Fully specificied filename of the output file.

    Examples
    --------
    """
    
    # Save the Data Container
    output_filename = instrument_data.save()
    
    # Validate the Data File
    validation_errors = validate(output_filename)
    
    if len(validation_errors) > 0:
        log.warning(f"Found validation errors in file ({output_filename}): {validation_errors}")
    else:
        log.info(f"Successfully wrote data to ({output_filename}) without validation errors.")
    
    return output_filename

def get_calibration_file(instrument_data: HermesData, time: astropy.time.Time = None) -> str:
    """
    Given a time, return the appropriate calibration file.

    Parameters
    ----------
    instrument_data: HermesData
        A data container in a logical data format
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
