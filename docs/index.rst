.. r-Daily-Programmer documentation master file, created by
   sphinx-quickstart on Wed May  6 11:32:46 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to |project|'s documentation!
=====================================

Quick-links
-----------

Source
''''''

Those who are not interested in documentation at all, but would rather see some source code,
can continue to my GitHub `r-daily-programmer <https://github.com/UltimateTimmeh/r-daily-programmer>`_
repository.

Documentation
'''''''''''''

Those who are not interested in scrolling through this introduction page to get to the part of
the documentation they are interested in can continue to the :ref:`modindex`, search for the
desired documentation using the :ref:`search` or make use of the following links, leading
to the documentation of the three main |project| packages:

.. toctree::
   :maxdepth: 2

   _apidoc/modules.rst

Introduction
------------

This is the documentation for my solutions to the challenges posted on `the /r/DailyProgrammer
subreddit <http://www.reddit.com/r/DailyProgrammer>`_. All programming is done in Python 3, and I
will attempt to always make my code as Pythonic as possible. The source can be consulted on GitHub,
in my `r-daily-programmer <https://github.com/UltimateTimmeh/r-daily-programmer>`_  repository.
If you have any questions, comments or suggestions, then feel free to send me a message on Reddit
(`/u/Ultimate_Timmeh <http://www.reddit.com/u/ultimate_timmeh>`_).

Challenges
----------

Challenge execution
'''''''''''''''''''

All challenge solutions are presented as modules. To execute one of the challenge modules you
should launch the ``dailyprogrammer.py`` script in a terminal with Python 3, and provide as
arguments the word 'execute' and the ID of the challenge you wish to execute. If the challenge
requires one or more input files, these files will be located in the directory
``dailyprogrammer/input/``. If the challenge is supposed to write output to a file, then this
file will be located in the directory ``dailyprogrammer/output/``.

Example -- Execute the solution to challenge '1 Easy - Ask Input' (ID 001e)::

    $ python3 dailyprogrammer.py execute 001e
    Name? > John Smith
    Age? > 50
    Reddit Username? > johnsmith
    Contents of User object:
        reddit_username: johnsmith
        age: 50
        name: John Smith
    Note: Data has been appended to file 'dailyprogrammer/output/001e_example_output.txt'

List of challenges
''''''''''''''''''

.. _asciiart: _apidoc/plugins.asciiart.html
.. _config: _apidoc/plugins.config.html
.. _doomsday: _apidoc/plugins.doomsday.html
.. _enhancedint: _apidoc/plugins.enhancedint.html
.. _enhancedstring: _apidoc/plugins.enhancedstring.html
.. _listtools: _apidoc/plugins.listtools.html
.. _password: _apidoc/plugins.password.html
.. _phonenumber: _apidoc/plugins.phonenumber.html
.. _textmenu: _apidoc/plugins.textmenu.html
.. _user: _apidoc/plugins.user.html
.. _utils: _apidoc/plugins.utils.html

.. _001e.doc: _apidoc/challenges.001e.html
.. _001e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/001e.py
.. _002e.doc: _apidoc/challenges.002e.html
.. _002e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/002e.py
.. _003e.doc: _apidoc/challenges.003e.html
.. _003e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/003e.py
.. _004e.doc: _apidoc/challenges.004e.html
.. _004e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/004e.py
.. _005e.doc: _apidoc/challenges.005e.html
.. _005e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/005e.py
.. _006e.doc: _apidoc/challenges.006e.html
.. _006e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/006e.py
.. _007e.doc: _apidoc/challenges.007e.html
.. _007e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/007e.py
.. _008e.doc: _apidoc/challenges.008e.html
.. _008e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/008e.py
.. _009e.doc: _apidoc/challenges.009e.html
.. _009e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/009e.py
.. _010e.doc: _apidoc/challenges.010e.html
.. _010e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/010e.py
.. _011e.doc: _apidoc/challenges.011e.html
.. _011e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/011e.py
.. _012e.doc: _apidoc/challenges.012e.html
.. _012e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/012e.py
.. _013e.doc: _apidoc/challenges.013e.html
.. _013e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/013e.py
.. _014e.doc: _apidoc/challenges.014e.html
.. _014e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/014e.py
.. _015e.doc: _apidoc/challenges.015e.html
.. _015e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/015e.py
.. _016e.doc: _apidoc/challenges.016e.html
.. _016e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/016e.py
.. _017e.doc: _apidoc/challenges.017e.html
.. _017e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/017e.py
.. _018e.doc: _apidoc/challenges.018e.html
.. _018e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/018e.py
.. _019e.doc: _apidoc/challenges.019e.html
.. _019e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/019e.py
.. _020e.doc: _apidoc/challenges.020e.html
.. _020e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/020e.py
.. _021e.doc: _apidoc/challenges.021e.html
.. _021e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/021e.py
.. _022e.doc: _apidoc/challenges.022e.html
.. _022e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/022e.py
.. _023e.doc: _apidoc/challenges.023e.html
.. _023e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/023e.py
.. _025e.doc: _apidoc/challenges.025e.html
.. _025e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/025e.py
.. _026e.doc: _apidoc/challenges.026e.html
.. _026e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/026e.py
.. _027e.doc: _apidoc/challenges.027e.html
.. _027e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/027e.py
.. _028e.doc: _apidoc/challenges.028e.html
.. _028e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/028e.py
.. _029e.doc: _apidoc/challenges.029e.html
.. _029e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/029e.py
.. _030e.doc: _apidoc/challenges.030e.html
.. _030e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/030e.py
.. _031e.doc: _apidoc/challenges.031e.html
.. _031e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/031e.py
.. _032e.doc: _apidoc/challenges.032e.html
.. _032e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/032e.py
.. _033e.doc: _apidoc/challenges.033e.html
.. _033e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/033e.py
.. _034e.doc: _apidoc/challenges.034e.html
.. _034e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/034e.py
.. _035e.doc: _apidoc/challenges.035e.html
.. _035e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/035e.py
.. _036e.doc: _apidoc/challenges.036e.html
.. _036e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/036e.py
.. _037e.doc: _apidoc/challenges.037e.html
.. _037e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/037e.py
.. _038e.doc: _apidoc/challenges.038e.html
.. _038e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/038e.py
.. _039e.doc: _apidoc/challenges.039e.html
.. _039e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/039e.py
.. _040e.doc: _apidoc/challenges.040e.html
.. _040e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/040e.py
.. _041e.doc: _apidoc/challenges.041e.html
.. _041e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/041e.py
.. _042e.doc: _apidoc/challenges.042e.html
.. _042e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/042e.py
.. _043e.doc: _apidoc/challenges.043e.html
.. _043e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/043e.py
.. _044e.doc: _apidoc/challenges.044e.html
.. _044e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/044e.py
.. _045e.doc: _apidoc/challenges.045e.html
.. _045e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/045e.py
.. _046e.doc: _apidoc/challenges.046e.html
.. _046e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/046e.py
.. _047e.doc: _apidoc/challenges.047e.html
.. _047e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/047e.py
.. _048e.doc: _apidoc/challenges.048e.html
.. _048e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/048e.py
.. _049e.doc: _apidoc/challenges.049e.html
.. _049e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/049e.py
.. _050e.doc: _apidoc/challenges.050e.html
.. _050e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/050e.py
.. _051e.doc: _apidoc/challenges.051e.html
.. _051e.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/051e.py

+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| Nr. | Difficulty | ID   | Name                       | Status*     | Documentation | Source    | Imported plugins                 |
+=====+============+======+============================+=============+===============+===========+==================================+
| 1   | Easy       | 001e | Ask Input                  | Complete    | 001e.doc_     | 001e.src_ | user_                            |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 2   | Easy       | 002e | Calculator                 | Complete    | 002e.doc_     | 002e.src_ | textmenu_                        |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 3   | Easy       | 003e | Caesar Cipher              | Complete    | 003e.doc_     | 003e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 4   | Easy       | 004e | Random Password            | Complete    | 004e.doc_     | 004e.src_ | password_                        |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 5   | Easy       | 005e | Password Protect           | Complete    | 005e.doc_     | 005e.src_ | password_, textmenu_, user_      |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 6   | Easy       | 006e | Calculate Pi               | Complete    | 006e.doc_     | 006e.src_ | textmenu_                        |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 7   | Easy       | 007e | Morse Code                 | Complete    | 007e.doc_     | 007e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 8   | Easy       | 008e | Beer Bottle                | Complete    | 008e.doc_     | 008e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 9   | Easy       | 009e | Sort Numbers               | Done        | 009e.doc_     | 009e.src_ | listtools_                       |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 10  | Easy       | 010e | Validate Phone Number      | Complete    | 010e.doc_     | 010e.src_ | phonenumber_                     |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 11  | Easy       | 011e | Doomsday Algorithm         | Complete    | 011e.doc_     | 011e.src_ | doomsday_                        |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 12  | Easy       | 012e | Permutations               | Complete    | 012e.doc_     | 012e.src_ | listtools_                       |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 13  | Easy       | 013e | Cumulative Day of the Year | Complete    | 013e.doc_     | 013e.src_ | doomsday_                        |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 14  | Easy       | 014e | Block Invert               | Complete    | 014e.doc_     | 014e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 15  | Easy       | 015e | Align Text                 | Complete    | 015e.doc_     | 015e.src_ | enhancedstring_                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 16  | Easy       | 016e | Remove Characters          | Complete    | 016e.doc_     | 016e.src_ | enhancedstring_                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 17  | Easy       | 017e | Text Triangle              | Complete    | 017e.doc_     | 017e.src_ | asciiart_                        |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 18  | Easy       | 018e | Easy Phone Number          | Complete    | 018e.doc_     | 018e.src_ | phonenumber_                     |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 19  | Easy       | 019e | Character Count            | Complete    | 019e.doc_     | 019e.src_ | enhancedstring_                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 20  | Easy       | 020e | Find Primes                | Complete    | 020e.doc_     | 020e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 21  | Easy       | 021e | Next Permutation           | Complete    | 021e.doc_     | 021e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 22  | Easy       | 022e | Merge Lists                | Complete    | 022e.doc_     | 022e.src_ | listtools_                       |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 23  | Easy       | 023e | Split Lists                | Complete    | 023e.doc_     | 023e.src_ | listtools_                       |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 25  | Easy       | 025e | Vote Counter               | Complete    | 025e.doc_     | 025e.src_ | listtools_                       |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 26  | Easy       | 026e | Filter String Duplicates   | Complete    | 026e.doc_     | 026e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 27  | Easy       | 027e | Year Info                  | Complete    | 027e.doc_     | 027e.src_ | doomsday_                        |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 28  | Easy       | 028e | Array Duplicate            | Complete    | 028e.doc_     | 028e.src_ | listtools_                       |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 29  | Easy       | 029e | Palindrome                 | Complete    | 029e.doc_     | 029e.src_ | enhancedstring_                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 30  | Easy       | 030e | Find Sum Pairs             | Complete    | 030e.doc_     | 030e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 31  | Easy       | 031e | Base 26 Multiplication     | Complete    | 031e.doc_     | 031e.src_ | enhancedint_                     |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 32  | Easy       | 032e | Roulette                   | Complete    | 032e.doc_     | 032e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 33  | Easy       | 033e | Study Tool                 | Complete    | 033e.doc_     | 033e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 34  | Easy       | 034e | Sum Of Squares             | Complete    | 034e.doc_     | 034e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 35  | Easy       | 035e | Number Triangle            | Complete    | 035e.doc_     | 035e.src_ | asciiart_                        |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 36  | Easy       | 036e | 1000 Lockers               | Complete    | 036e.doc_     | 036e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 37  | Easy       | 037e | File Line Count            | Complete    | 037e.doc_     | 037e.src_ | enhancedstring_                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 38  | Easy       | 038e | Dijkstra's Algorithm       | Complete    | 038e.doc_     | 038e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 39  | Easy       | 039e | FizzBuzz                   | Complete    | 039e.doc_     | 039e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 40  | Easy       | 040e | Alternative Counting       | Complete    | 040e.doc_     | 040e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 41  | Easy       | 041e | ASCII Framing              | Complete    | 041e.doc_     | 041e.src_ | enhancedstring_                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 42  | Easy       | 042e | Beer Bottle 2              | Complete    | 042e.doc_     | 042e.src_ | enhancedint_                     |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 43  | Easy       | 043e | Lowest Common Ancestor     | Complete    | 043e.doc_     | 043e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 44  | Easy       | 044e | Split Sentences            | Complete    | 044e.doc_     | 044e.src_ | enhancedstring_                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 45  | Easy       | 045e | Checkered Grid             | Complete    | 045e.doc_     | 045e.src_ | asciiart_                        |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 46  | Easy       | 046e | Population Count           | Complete    | 046e.doc_     | 046e.src_ | enhancedint_                     |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 47  | Easy       | 047e | Caesar Cipher 2            | Complete    | 047e.doc_     | 047e.src_ |                                  |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 48  | Easy       | 048e | Evensort                   | Complete    | 048e.doc_     | 048e.src_ | listtools_                       |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 49  | Easy       | 049e | Monty Hall Problem         | Complete    | 049e.doc_     | 049e.src_ | listtools_                       |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 50  | Easy       | 050e | First Sum Pair             | Complete    | 050e.doc_     | 050e.src_ | listtools_                       |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+
| 51  | Easy       | 051e | Combinations               | Complete    | 051e.doc_     | 051e.src_ | listtools_                       |
+-----+------------+------+----------------------------+-------------+---------------+-----------+----------------------------------+

\*\ **Challenge status**:

- *In progress*: started but not yet done
- *Done*: main challenge finished, but not the extra credit(s)
- *Complete*: main challenge and extra credit(s) finished

Plugins
-------

Motivation for the creation of plugins
''''''''''''''''''''''''''''''''''''''

Many of the challenges lead to code that might be useful in future challenges. Because of this,
in some cases it makes sense to package part of the solution to a challenge as a *plugin* that
can also be imported in future challenge execution modules.

List of plugins
'''''''''''''''

.. _asciiart.doc: _apidoc/plugins.asciiart.html
.. _asciiart.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/asciiart.py
.. _config.doc: _apidoc/plugins.config.html
.. _config.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/config.py
.. _doomsday.doc: _apidoc/plugins.doomsday.html
.. _doomsday.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/doomsday.py
.. _enhancedint.doc: _apidoc/plugins.enhancedint.html
.. _enhancedint.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/enhancedint.py
.. _enhancedstring.doc: _apidoc/plugins.enhancedstring.html
.. _enhancedstring.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/enhancedstring.py
.. _listtools.doc: _apidoc/plugins.listtools.html
.. _listtools.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/listtools.py
.. _password.doc: _apidoc/plugins.password.html
.. _password.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/password.py
.. _phonenumber.doc: _apidoc/plugins.phonenumber.html
.. _phonenumber.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/phonenumber.py
.. _textmenu.doc: _apidoc/plugins.textmenu.html
.. _textmenu.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/textmenu.py
.. _user.doc: _apidoc/plugins.user.html
.. _user.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/user.py
.. _utils.doc: _apidoc/plugins.utils.html
.. _utils.src: http://www.github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/utils.py

+----------------+---------------------+---------------------+
| Name           | Documentation       | Source              |
+================+=====================+=====================+
| asciiart       | asciiart.doc_       | asciiart.src_       |
+----------------+---------------------+---------------------+
| config         | config.doc_         | config.src_         |
+----------------+---------------------+---------------------+
| doomsday       | doomsday.doc_       | doomsday.src_       |
+----------------+---------------------+---------------------+
| enhancedint    | enhancedint.doc_    | enhancedint.src_    |
+----------------+---------------------+---------------------+
| enhancedstring | enhancedstring.doc_ | enhancedstring.src_ |
+----------------+---------------------+---------------------+
| listtools      | listtools.doc_      | listtools.src_      |
+----------------+---------------------+---------------------+
| password       | password.doc_       | password.src_       |
+----------------+---------------------+---------------------+
| phonenumber    | phonenumber.doc_    | phonenumber.src_    |
+----------------+---------------------+---------------------+
| textmenu       | textmenu.doc_       | textmenu.src_       |
+----------------+---------------------+---------------------+
| user           | user.doc_           | user.src_           |
+----------------+---------------------+---------------------+
| utils          | utils.doc_          | utils.src_          |
+----------------+---------------------+---------------------+

Testing
-------

Because testing code is not only good practice, but also required in a professional environment, I
decided to include it in this project. Plugins are used in multiple challenges and are often subject
to change, so I decided to write a unit test module for each plugin combined with one execution test
module for testing the execution of *all* challenge modules. These test modules are located in the
directory ``dailyprogrammer/tests``. Testing is performed using Python's standard ``unittest`` and
``mock`` libraries. Tests can be executed by running the ``dailyprogrammer.py`` script with Python
3, providing the arguments 'runtests' followed by the desired name of the resulting log file. By
default, log files are placed in ``dailyprogrammer/tests/logs``.

Example -- Execute all tests and write the output to 'tests.log'::

    $ python3 dailyprogrammer.py runtests tests.log
