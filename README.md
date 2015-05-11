# r-daily-programmer

## Introduction

My repository for solutions to the challenges posted on [the /r/DailyProgrammer subreddit](http://www.reddit.com/r/DailyProgrammer).
All programming is done using Python 3, and I will attempt to always make all my code as pythonic
as possible. If you have any comments or suggestions, feel free to send me a message!

## Challenges

**Challenge execution**

All challenge solutions are presented as modules. To execute one of the challenge modules you should
launch the `dailyprogrammer.py` script in a terminal with python3, and provide as argument the ID of the
desired challenge. If the challenge is supposed to write output to a file, then this file will be
located in the directory `dailyprogrammer/output/`.

*Example - Execute the solution for challenge '001e - Ask Input'*

    $ python3 dailyprogrammer.py 001e
    Name? > John Smith
    Age? > 50
    Reddit Username? > johnsmith
    Contents of User object:
        reddit_username: johnsmith
        age: 50
        name: John Smith
    Note: Data has been appended to file '/path/to/project/dailyprogrammer/output/001e_example_output.txt'

**Info about challenge status**

- *In progress*: Started, but not yet done.
- *Done*: Main challenge finished, but not the extra credit(s).
- *Complete*: Main challenge and extra credits finished.

**List of challenges**

- *001e* - [Ask Input](dailyprogrammer/challenges/001e.py): Complete
- *002e* - [Calculator](dailyprogrammer/challenges/002e.py): Complete
- *003e* - [Caesar Cipher](dailyprogrammer/challenges/003e.py): Complete
- *004e* - [Random Password](dailyprogrammer/challenges/004e.py): Complete
- *005e* - [Password Protect](dailyprogrammer/challenges/005e.py): Complete
- *006e* - [Calculate Pi](dailyprogrammer/challenges/006e.py): Complete

## Plugins

**Description**

Many of the challenges have objectives in them that can be (partially) solved by making use of the
solution of previous challenges. Because of this, it makes sense to create *plugins* that can be
imported in the challenge execution scripts.

**Testing**

Plugins will be tested with Python's `unittest` package. Unit tests for all plugins that have them
can be executed by using the 'discover' functionality of Python's unittest in the `dailyprogrammer`
directory. For example, to execute all unit tests in the DailyProgrammer project and store the
results to a log file, you could use the command:

    $ python3 -m unittest discover -v > path_to_log_file.log 2>&1

**List of plugins**

- [cipher](dailyprogrammer/plugins/cipher.py)
- [config](dailyprogrammer/plugins/config.py)
- [formula](dailyprogrammer/plugins/formula.py)
- [password](dailyprogrammer/plugins/password.py)
- [pi](dailyprogrammer/plugins/pi.py)
- [textmenu](dailyprogrammer/plugins/textmenu.py)
- [user](dailyprogrammer/plugins/user.py)

## Documentation

All code in this project is documented through the docstrings as well as I am able. All docstring
documentation can be automatically bundled as reStructuredText in the `docs` directory and then
converted into nice HTML doumentation using Sphinx. If you are interested in doing this, then you
should follow [this link](docs/README.md) for instructions.
