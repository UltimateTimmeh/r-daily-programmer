#!/usr/bin/python3
"""
Unit tests for module :mod:`plugins.cipher`.
"""

import unittest

from plugins import cipher


class TestCipherFunctions(unittest.TestCase):
    """Unit tests for functions in module :mod:`plugins.cipher`."""


    def test_caesar(self):
        """Test function :func:`plugins.cipher.caesar`

        **Tested:**

        - The returned encoded message is correct.
        - The returned decoded message is correct.
        """
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
        """Test function :func:`plugins.cipher.caesar_brute_force`

        **Tested:**

        - The returned list of decoding possibilities is correct.
        """
        msg_encoded = 'havggrfg'
        result = cipher.caesar_brute_force(msg_encoded)
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
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
