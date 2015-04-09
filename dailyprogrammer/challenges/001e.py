#!/usr/bin/python3
"""
Main execution script for challenge '001Easy - Ask Input'.
"""

import os
import plugins.config as cfg
from plugins.personalinfo import PersonalInfo


def run():
    # Ask for input.
    name = input("Name? > ")
    age = input("Age? > ")
    reddit_username = input("Reddit Username? > ")

    # Create PersonalInfo object, print and write to file.
    pi = PersonalInfo(name, age, reddit_username=reddit_username)
    print(pi)
    outputfile_fn = os.path.join(cfg.output_dir, '001e_example_output.txt')
    pi.write(outputfile_fn)
