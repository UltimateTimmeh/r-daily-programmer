## Documentation - HowTo

To automatically generate the HTML documentation for this project, open a terminal in the directory
where this file is located and execute the following two commands:

    $ sphinx-apidoc -feo _apidoc ../dailyprogrammer ../dailyprogrammer/dailyprogrammer.py
    $ make html

This will generate HTML documentation for the DailyProgrammer project, which can be viewed in any
web browser by opening the file `_build/html/index.html`.
