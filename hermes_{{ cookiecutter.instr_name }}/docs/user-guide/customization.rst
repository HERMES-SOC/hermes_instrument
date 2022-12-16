.. _customization:

**************************************
Customization and Global Configuration
**************************************

The :file:`configrc` file
=========================

This package uses a :file:`configrc` configuration file to customize certain properties.
You can control a number of key features such as where your data will download to. 
This configuration file in a platform specific directory, which you can see the path for by running::

  >>> import hermes_{{ cookiecutter.instr_name }}
  >>> hermes_{{ cookiecutter.instr_name }}.print_config()  # doctest: +SKIP


To maintain your own customizations place a copy of the default file into the *first* path printed above.
Do not edit the default file directly as every time you install or update, this file will be overwritten.

See below for the example config file.

.. _customizing-with-dynamic-settings:

Dynamic settings
================

You can also dynamically change the default settings in a Python script or
interactively from the python shell. All of the settings are stored in a
Python ConfigParser instance called ``sunpy.config``, which is global to
the package. Settings can be modified directly, for example::

    import hermes_{{ cookiecutter.instr_name }}
    hermes_{{ cookiecutter.instr_name }}.config.set('downloads', 'download_dir', '/home/user/Downloads')


.. configrc-sample:

A sample configrc file
--------------------------------------------------------------------

.. only:: html

    `(download) <../_static/configrc>`__

.. literalinclude:: ../../hermes_{{ cookiecutter.instr_name }}/data/configrc