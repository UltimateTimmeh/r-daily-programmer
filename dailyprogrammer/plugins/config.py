#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/config.py

Configurable variables used in |project| (source_).

| **plugins_dir** (str) -- directory containing the |project| plugin modules
| **root_dir** (str) -- root directory of |project|
| **output_dir** (str) -- directory for storing |project| challenge output files
| **tmp_dir** (str) -- temporary directory for storing |project| unit test input and output files
"""
import os

# Directories.
plugins_dir = os.path.split(__file__)[0]
root_dir = os.path.abspath(os.path.join(plugins_dir, '..'))
output_dir = os.path.join(root_dir, 'output')
tmp_dir = os.path.join(root_dir, 'tests', 'tmp')
