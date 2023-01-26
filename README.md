# hermes_instrument
A [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) Python package template for the hermes instrument packages.

Any changes made to this template will be applied to the instrument packages through [cruft](https://cruft.github.io/cruft/).

## Instructions for Maintainers

### Building the template

To build this template into a Python package, first clone this repository. In the directory that contains the hermes_instrument folder, run

    cookiecutter hermes_instrument

Answer the instrument prompt. If you named your instrument 'boo', then cookiecutter will create a new directory called `hermes_boo`. Go into this directory and run

    git init

This is required by `setuptools_scm` to be able to derive the version number automatically. You can then install the package with

    pip install -e .

