#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/tests/test_challenges.py

Tests for successful and/or correct execution of all :mod:`challenges` (source_).
"""

import importlib
import mock
import os
import shutil
import unittest

import plugins.config


class GetInputMock(mock.Mock):
    """A mock get_input object.

    This object is meant to mock the :func:`plugins.utils.get_input` function. On top of returning
    the value you want it to return, it also prints the first argument it was called with followed
    by the return value. As can be seen in the example below, this replicates the printing behavior
    of the :func:`plugins.utils.get_input` function instead of merely returning the assigned return
    value. The sole reason this behavior is desired is to make the automatic challenge execution
    tests print the same output as when executing the challenges normally (also see the example runs
    on the challenge documentation pages).

    Example::

        >>> from plugins.utils import get_input
        >>> result = get_input("Input request > ")  ## Here the user has to type the response himself.
        Input request > answer
        >>> print(result)
        answer
        >>> from mock import Mock
        >>> get_input = Mock(return_value='answer')
        >>> result = get_input("Input request > ")  ## Nothing is printed when calling this mock object.
        >>> print(result)
        answer
        >>> from tests.test_challenge_execution import GetInputMock
        >>> get_input = GetInputMock(return_value='answer')
        >>> result = get_input("Input request > ")  ## When calling this mock object, the printing behavior of 'get_input' is replicated.
        Input request > answer
        >>> print(result)
        answer
    """


    def __call__(self, *args, **kwargs):
        """Call the mock object."""
        if args:
            print(args[0], end='')
        return_value = super().__call__(*args, **kwargs)
        print(return_value)
        return return_value



class TestChallenges(unittest.TestCase):
    """Execution tests for all :mod:`challenges`."""


    def setUp(self):
        """Setup before test.

        Set test configuration and create directories for temporarily storing test input
        and output files (see :mod:`plugins.config`).
        """
        # Backup configuration and set configuration for testing.
        self.cfg_ = plugins.config
        plugins.config.output_dir = os.path.join(plugins.config.tmp_dir, 'output')
        # Create input/output directories.
        os.makedirs(plugins.config.output_dir, exist_ok=True)


    def tearDown(self):
        """Teardown after test.

        Reset configuration. If it exists, recursively remove the directories for temporarily
        storing test input and output files (see :meth:`tests.test_challenges.TestChallenges.setUp`).
        """
        # Remove input/output directories.
        if os.path.isdir(plugins.config.tmp_dir):
            shutil.rmtree(plugins.config.tmp_dir)
        # Reset configuration.
        plugins.config = self.cfg_


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_001e(self, inputm):
        """Challenge 001e is executed successfully and correctly"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 001 EASY ===\n")
        challenge = importlib.import_module('challenges.001e')
        inputm.side_effect = ['John Smith', '50', 'johnsmith']
        challenge.run()
        # Test correct execution.
        outfp = os.path.join(plugins.config.output_dir, '001e_example_output.txt')
        with open(outfp, 'r') as outfile:
            result = outfile.read()
        expected = [
            "Contents of User object:",
            "name: John Smith",
            "age: 50",
            "username: johnsmith",
        ]
        self.assertTrue(all([part in result for part in expected]))


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_002e(self, inputm):
        """Challenge 002e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 002 EASY ===\n")
        challenge = importlib.import_module('challenges.002e')
        inputm.side_effect = ['1', '2', '2', '10', '', 'q']
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_003e(self, inputm):
        """Challenge 003e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 003 EASY ===\n")
        challenge = importlib.import_module('challenges.003e')
        inputm.side_effect = ['dailyprogrammer', '5']
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_004e(self, inputm):
        """Challenge 004e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 004 EASY ===\n")
        challenge = importlib.import_module('challenges.004e')
        inputm.side_effect = ['5', '20']
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_005e(self, inputm):
        """Challenge 005e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 005 EASY ===\n")
        challenge = importlib.import_module('challenges.005e')
        inputm.side_effect = [
            '3', '',
            '2', 'johnsmith', 'password',
            '1', 'johnsmith', 'password', '',
            '3', '',
            'q',
        ]
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_006e(self, inputm):
        """Challenge 006e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 006 EASY ===\n")
        challenge = importlib.import_module('challenges.006e')
        inputm.side_effect = ['1', '30', 'q']
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_007e(self, inputm):
        """Challenge 007e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 007 EASY ===\n")
        challenge = importlib.import_module('challenges.007e')
        inputm.side_effect = ['WHAT HATH GOD WROUGHT', 'n']
        challenge.run()


    def test_challenge_008e(self):
        """Challenge 008e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 008 EASY ===\n")
        challenge = importlib.import_module('challenges.008e')
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_009e(self, inputm):
        """Challenge 009e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 009 EASY ===\n")
        challenge = importlib.import_module('challenges.009e')
        inputm.side_effect = ['1.2, 325.0, 2, 5.6, 2.0, -3.75', 'merge']
        challenge.run()


    def test_challenge_010e(self):
        """Challenge 010e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 010 EASY ===\n")
        challenge = importlib.import_module('challenges.010e')
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_011e(self, inputm):
        """Challenge 011e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 011 EASY ===\n")
        challenge = importlib.import_module('challenges.011e')
        inputm.side_effect = ['2015', '5', '13']
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_012e(self, inputm):
        """Challenge 012e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 012 EASY ===\n")
        challenge = importlib.import_module('challenges.012e')
        inputm.side_effect = ['hi!']
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_013e(self, inputm):
        """Challenge 013e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 013 EASY ===\n")
        challenge = importlib.import_module('challenges.013e')
        inputm.side_effect = [
            '2015', '5', '18',
            '2016', '2', '29',
        ]
        challenge.run()
        challenge.run()


    def test_challenge_014e(self):
        """Challenge 014e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 014 EASY ===\n")
        challenge = importlib.import_module('challenges.014e')
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_015e(self, inputm):
        """Challenge 015e is executed successfully and correctly"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 015 EASY ===\n")
        challenge = importlib.import_module('challenges.015e')
        inputm.side_effect = ['015e_example_input.txt', '^', '015e_example_output.txt']
        challenge.run()
        # Test correct execution.
        outfp = os.path.join(plugins.config.output_dir, '015e_example_output.txt')
        with open(outfp, 'r') as outfile:
            result = outfile.read()
        expected = '\n'.join([
            "           Short line 1",
            "           Short line 2",
            "        A bit longer line 1",
            "           Short line 3",
            "        A bit longer line 2",
            " This is very long line number one",
            " This is very long line number two",
            "        A bit longer line 3",
            "This is very long line number three",
            "",
        ])
        self.assertEqual(result, expected)


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_016e(self, inputm):
        """Challenge 016e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 016 EASY ===\n")
        challenge = importlib.import_module('challenges.016e')
        inputm.side_effect = ['Daily Programmer', 'ae iou']
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_017e(self, inputm):
        """Challenge 017e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 017 EASY ===\n")
        challenge = importlib.import_module('challenges.017e')
        inputm.side_effect = ['6']
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_018e(self, inputm):
        """Challenge 018e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 018 EASY ===\n")
        challenge = importlib.import_module('challenges.018e')
        inputm.side_effect = ['1-800-COMCAST']
        challenge.run()


    @unittest.skipIf(not plugins.config.testlong, "plugins.config.testlong is False")
    def test_challenge_019e(self):
        """Challenge 019e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 019 EASY ===\n")
        challenge = importlib.import_module('challenges.019e')
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_020e(self, inputm):
        """Challenge 020e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 020 EASY ===\n")
        challenge = importlib.import_module('challenges.020e')
        inputm.side_effect = ['2000']
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_021e(self, inputm):
        """Challenge 021e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 021 EASY ===\n")
        challenge = importlib.import_module('challenges.021e')
        inputm.side_effect = ['93765.44321']
        challenge.run()


    def test_challenge_022e(self):
        """Challenge 022e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 022 EASY ===\n")
        challenge = importlib.import_module('challenges.022e')
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_023e(self, inputm):
        """Challenge 023e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 023 EASY ===\n")
        challenge = importlib.import_module('challenges.023e')
        inputm.side_effect = ['10', '0.5']
        challenge.run()


    def test_challenge_025e(self):
        """Challenge 025e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 025 EASY ===\n")
        challenge = importlib.import_module('challenges.025e')
        challenge.run()


    def test_challenge_026e(self):
        """Challenge 026e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 026 EASY ===\n")
        challenge = importlib.import_module('challenges.026e')
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_027e(self, inputm):
        """Challenge 027e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 027 EASY ===\n")
        challenge = importlib.import_module('challenges.027e')
        inputm.side_effect = ['1996', '1900']
        challenge.run()
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_028e(self, inputm):
        """Challenge 028e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 028 EASY ===\n")
        challenge = importlib.import_module('challenges.028e')
        inputm.side_effect = [
            '10', '1', '1000000', 'y',
            '1000000', '1', '2000000', 'n',
        ]
        challenge.run()
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_029e(self, inputm):
        """Challenge 029e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 029 EASY ===\n")
        challenge = importlib.import_module('challenges.029e')
        inputm.side_effect = ['hannah', 'hennah']
        challenge.run()
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_030e(self, inputm):
        """Challenge 030e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 030 EASY ===\n")
        challenge = importlib.import_module('challenges.030e')
        inputm.side_effect = [
            '10', '0', '1', '3',
            '20', '0', '10', '10',
        ]
        challenge.run()
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_031e(self, inputm):
        """Challenge 031e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 031 EASY ===\n")
        challenge = importlib.import_module('challenges.031e')
        inputm.side_effect = ['CSGHJ', 'CBA']
        challenge.run()


    @mock.patch('random.sample')
    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_032e(self, inputm, samplem):
        """Challenge 032e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 032 EASY ===\n")
        challenge = importlib.import_module('challenges.032e')
        inputm.side_effect = [
            '1', 'John', '2000', '2100',
            '2000,r1+b2+r7+b8', '1000,r1+b2+b4+r5;1000,red', '', '', '', '', '', '', '', '', '',
            '2000,red', '', '', '', '', '', '', '', '',
        ]
        samplem.side_effect = [
            ['r21'], ['r27'],
        ]
        challenge.run()


    @mock.patch('random.shuffle')
    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_033e(self, inputm, shufflem):
        """Challenge 033e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 033 EASY ===\n")
        challenge = importlib.import_module('challenges.033e')
        inputm.side_effect = ['144', 'website without cats', 'hello', 'exit']
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_034e(self, inputm):
        """Challenge 034e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 034 EASY ===\n")
        challenge = importlib.import_module('challenges.034e')
        inputm.side_effect = ['9,2,6']
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_035e(self, inputm):
        """Challenge 035e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 035 EASY ===\n")
        challenge = importlib.import_module('challenges.035e')
        inputm.side_effect = ['6', '12', '15', '150']
        challenge.run()
        challenge.run()
        challenge.run()
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_036e(self, inputm):
        """Challenge 036e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 036 EASY ===\n")
        challenge = importlib.import_module('challenges.036e')
        inputm.side_effect = ['1000']
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_037e(self, inputm):
        """Challenge 037e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 037 EASY ===\n")
        challenge = importlib.import_module('challenges.037e')
        inputm.side_effect = ['037e_example_input.txt']
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_038e(self, inputm):
        """Challenge 038e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 038 EASY ===\n")
        challenge = importlib.import_module('challenges.038e')
        inputm.side_effect = ['A', 'I']
        challenge.run()


    def test_challenge_039e(self):
        """Challenge 039e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 039 EASY ===\n")
        challenge = importlib.import_module('challenges.039e')
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_040e(self, inputm):
        """Challenge 040e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 040 EASY ===\n")
        challenge = importlib.import_module('challenges.040e')
        inputm.side_effect = ['1', '1001', '1']
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_041e(self, inputm):
        """Challenge 041e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 041 EASY ===\n")
        challenge = importlib.import_module('challenges.041e')
        inputm.side_effect = [
            "So long, and thanks for all the fish!",
            ("This is a very long line which is surely going to be split "
             "into multiple lines after typing it all!"),
        ]
        challenge.run()
        challenge.run()


    def test_challenge_042e(self):
        """Challenge 042e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 042 EASY ===\n")
        challenge = importlib.import_module('challenges.042e')
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_043e(self, inputm):
        """Challenge 043e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 043 EASY ===\n")
        challenge = importlib.import_module('challenges.043e')
        inputm.side_effect = ['d', 'h']
        challenge.run()


    def test_challenge_044e(self):
        """Challenge 044e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 044 EASY ===\n")
        challenge = importlib.import_module('challenges.044e')
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_045e(self, inputm):
        """Challenge 045e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 045 EASY ===\n")
        challenge = importlib.import_module('challenges.045e')
        inputm.side_effect = ['8', '8', '3', '2', '░ █']
        challenge.run()


    @mock.patch('plugins.utils.get_input', new_callable=GetInputMock)
    def test_challenge_046e(self, inputm):
        """Challenge 046e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 046 EASY ===\n")
        challenge = importlib.import_module('challenges.046e')
        inputm.side_effect = ['0', '23', '15698', '123456789', 'q']
        challenge.run()


    def test_challenge_047e(self):
        """Challenge 047e is executed successfully"""
        # Test successful execution.
        print("\n=== EXECUTING CHALLENGE 047 EASY ===\n")
        challenge = importlib.import_module('challenges.047e')
        challenge.run()


if __name__ == '__main__':
    unittest.main()
