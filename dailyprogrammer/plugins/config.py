#!/usr/bin/python3
"""
Configuration for package dailyprogrammer
"""
import os

# Directories.
plugins_dir = os.path.split(__file__)[0]
package_dir = os.path.abspath(os.path.join(plugins_dir, '..'))
output_dir = os.path.join(package_dir, 'output')
tmp_dir = os.path.join(package_dir, 'tests', 'tmp')
