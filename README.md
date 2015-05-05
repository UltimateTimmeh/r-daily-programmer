# r-daily-programmer

## Introduction

My repository for solutions to the challenges posted on [the /r/DailyProgrammer subreddit](http://www.reddit.com/r/DailyProgrammer).
All programming is done using python 3.x, and I will attempt to always make all my code as pythonic
as possible. If you have any comments or suggestions, feel free to send me a message!

## Challenges

**Challenge execution**

To execute one of the challenge solutions you should launch the `dailyprogrammer.py` script in a
shell with python 3, with as argument the id of the desired challenge. If the challenge is supposed
to write output to a file, then this file will be located in the directory
`dailyprogrammer/output/`.

*Example - Execute the solution for challenge '001e - Ask Input'*

    $ python3 dailyprogrammer.py 001e
    Name? > John Smith
    Age? > 50
    Reddit Username? > John_Smith
    Personal information of John Smith (50 years old):
        reddit_username: John_Smith
        name: John Smith
        age: 50

*(Note: The output that is printed at the end of this challenge should also have been appended to
the file `dailyprogrammer/output/001e_example_output.txt`)*

**Info about challenge status**

- *In progress*: Started, but not yet done.
- *Done*: Main challenge finished, but not the extra credit(s).
- *Complete*: Main challenge and extra credits finished.

**List of challenges**

- *001e* - [Ask Input](doc/challenges/001e_askinput.md): Complete
- *002e* - [Calculator](doc/challenges/002e_calculator.md): Complete
- *003e* - [Caesar Cipher](doc/challenges/003e_caesarcipher.md): Complete
- *004e* - [Random Password](doc/challenges/004e_randompassword.md): Complete

## Plugins

**Description**

Many of the challenges have objectives in them that can be (partially) solved by making use of the
solution of previous challenges. Because of this, it makes sense to create *plugins* that can be
imported in the challenge execution scripts.

**Testing**

Plugins will be tested with Python's `unittest` package. Unit tests for all plugins that have them
can be executed by using the 'discover' functionality of Python's unittest in the `dailyprogrammer`
directory. To store the output of the test run in a log file, for example, you should use the
command:

    $ python3 -m unittest discover -v > path_to_log_file.log 2>&1

**List of plugins**

- [authentication](doc/plugins/authentication.md)
- [cipher](doc/plugins/cipher.md)
- [config](doc/plugins/config.md)
- [formula](doc/plugins/formula.md)
- [personalinfo](doc/plugins/personalinfo.md)
- [textmenu](doc/plugins/textmenu.md)
