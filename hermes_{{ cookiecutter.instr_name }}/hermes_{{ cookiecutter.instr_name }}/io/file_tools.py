"""
This module provides a generic file reader.
"""
import os.path
from pathlib import Path

import ccsdspy

from hermes_core.util.util import create_science_filename, parse_science_filename
from hermes_core.timedata import HermesData
from hermes_core.util.validation import validate

from hermes_{{ cookiecutter.instr_name }} import log
import hermes_{{ cookiecutter.instr_name }}

__all__ = [
    "load_data_file",
    "parse_l0_sci_packets",
    "read_calibration_file",
    "write_data_file",
]


def load_data_file(data_filename: Path) -> HermesData:
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
    log.info(f"Loading Data File: {data_filename}.")

    # Get Filename Information
    file_metadata = parse_science_filename(data_filename.name)

    # check if level 0 binary file, if so call appropriate functions
    if file_metadata["level"] == "l0":
        instrument_data = parse_l0_sci_packets(data_filename)
    # If not level 0 binary file, load as a CDF file
    else:
        # As an example, you can load CDF files directly into the data container
        instrument_data = HermesData.load(data_filename)

    return instrument_data


def parse_l0_sci_packets(data_filename: Path) -> HermesData:
    """
    Parse a level 0 binary file containing CCSDS packets.

    Parameters
    ----------
    data_filename: str
        Fully specificied filename of l0 packet file

    Returns
    -------
    instrument_data: HermesData
        A data container in a logical data format containing the l0 data

    Examples
    --------
    """
    log.info(f"Parsing packets from file:{data_filename}.")

    pkt = ccsdspy.FixedLength.from_file(
        os.path.join(hermes_{{ cookiecutter.instr_name }}._data_directory, "sci_packet_def.csv")
    )
    data = pkt.load(data_filename)
    
    # Process the Packet dict to create a HermesData data container
    # NOTE: Template does no transormations here.
    instrument_data = None
    
    return instrument_data


def read_calibration_file(calib_filename: Path) -> Path:
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
    return None


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
        log.warning(
            f"Found validation errors in file ({output_filename}): {validation_errors}"
        )
    else:
        log.info(
            f"Successfully wrote data to ({output_filename}) without validation errors."
        )
    return output_filename
