#!/usr/bin/python3
"""
Configurable variables used in |project|.

Directories
-----------

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
