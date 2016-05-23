#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/config.py

Configurable variables used in |project| (source_).

| *var* plugins.config.\ **plugins_dir** (str)
|     directory containing the |project| plugin modules

| *var* plugins.config.\ **root_dir** (str)
|     root directory of |project|

| *var* plugins.config.\ **input_dir** (str)
|     directory for storing |project| challenge input files

| *var* plugins.config.\ **output_dir** (str)
|     directory for storing |project| challenge output files

| *var* plugins.config.\ **tests_dir** (str)
|     directory containing the |project| unit tests

| *var* plugins.config.\ **logs_dir** (str)
|     directory containing the |project| unit test logs

| *var* plugins.config.\ **tmp_dir** (str)
|     directory for temporarily storing unit test input and output files

| *var* plugins.config.\ **testlong** (bool)
|     indicates whether or not to perform execution tests of time-consuming challenges
"""

import os

# Directories.
plugins_dir = os.path.split(__file__)[0]
root_dir = os.path.abspath(os.path.join(plugins_dir, '..'))
input_dir = os.path.join(root_dir, 'input')
output_dir = os.path.join(root_dir, 'output')
tests_dir = os.path.join(root_dir, 'tests')
logs_dir = os.path.join(tests_dir, 'logs')
tmp_dir = os.path.join(tests_dir, 'tmp')

#Other variables
testlong = False
