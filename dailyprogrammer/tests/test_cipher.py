#!/usr/bin/python3
"""
Unit tests for plugin cipher
"""

import unittest

from plugins import cipher


class TestCipher(unittest.TestCase):
    """Unit tests for functions in plugin cipher"""


    def setUp(self):
        """Set up before test"""
        pass


    def tearDown(self):
        """Tear down after test"""
        pass


    def test_caesar(self):
        """Test function cipher.caesar"""
        datapoints = [
            ('testmsg', 0, 'testmsg'),
            ('testmsg', 13, 'grfgzft'),
            ('testmsg', 30, 'xiwxqwk'),
            ]
        for data in datapoints:
            decoded_expected, n, encoded_expected = data
            encoded = cipher.caesar(decoded_expected, n)
            decoded = cipher.caesar(encoded_expected, n, dir='decode')
            self.assertEqual(encoded, encoded_expected)
            self.assertEqual(decoded, decoded_expected)


    def test_caesar_brute_force(self):
        """Test function cipher.caesar_brute_force"""
        msg_encoded = 'havggrfg'
        expected = [
            'havggrfg',
            'gzuffqef',
            'fyteepde',
            'exsddocd',
            'dwrccnbc',
            'cvqbbmab',
            'bupaalza',
            'atozzkyz',
            'zsnyyjxy',
            'yrmxxiwx',
            'xqlwwhvw',
            'wpkvvguv',
            'vojuuftu',
            'unittest',
            'tmhssdrs',
            'slgrrcqr',
            'rkfqqbpq',
            'qjeppaop',
            'pidoozno',
            'ohcnnymn',
            'ngbmmxlm',
            'mfallwkl',
            'lezkkvjk',
            'kdyjjuij',
            'jcxiithi',
            'ibwhhsgh',
            ]
        result = cipher.caesar_brute_force(msg_encoded)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
