#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/cipher.py

Encoding and decoding messages using ciphers (source_).
"""


def caesar(msg, rs, dir='encode'):
    """Encode or decode a message using the caesar cipher.

    :param str msg: message that will be encoded or decoded
    :param int rs: amount of right shift used for encoding or decoding the message
    :param str dir: cipher direction, one of ['encode', 'decode'] (default 'encode')
    :return: encoded or decoded message
    :rtype: str

    Example::

        >>> from cipher import caesar
        >>> msg = 'DailyProgrammer'
        >>> caesar(msg, 10)
        'nksvizbyqbkwwob'
        >>> msg = 'qnvylcebtenzzre'
        >>> caesar(msg, 13, dir='decode')
        'dailyprogrammer'
    """
    # Process arguments.
    msg = msg.lower()
    rs = rs % 26
    if dir == 'decode':
        rs = -rs

    # Create cipher map.
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abc_shift = abc[rs:] + abc[:rs]
    cipher_map = {c: c_s for c, c_s in zip(abc, abc_shift)}

    # Process message and return result.
    msg_shift = ''
    for cc in msg:
        if cc in abc:
            msg_shift += cipher_map[cc]
        else:
            msg_shift += cc
    return msg_shift


def caesar_brute_force(msg_encoded):
    """Return all possible options for decoding a caesar-cipher-endoded message.

    :param str msg_encoded: encoded message that will be brute-force-decoded
    :return: list containing all possible options for decoding the encoded message
    :rtype: list(str,...)

    Example::

        >>> from cipher import caesar_brute_force
        >>> msg = 'qnvylcebtenzzre'
        >>> print('\\n'.join(caesar_brute_force(msg)))
        qnvylcebtenzzre
        pmuxkbdasdmyyqd
        oltwjaczrclxxpc
        nksvizbyqbkwwob
        mjruhyaxpajvvna
        liqtgxzwoziuumz
        khpsfwyvnyhttly
        jgorevxumxgsskx
        ifnqduwtlwfrrjw
        hempctvskveqqiv
        gdlobsurjudpphu
        fcknartqitcoogt
        ebjmzqsphsbnnfs
        dailyprogrammer
        czhkxoqnfqzlldq
        bygjwnpmepykkcp
        axfivmoldoxjjbo
        zwehulnkcnwiian
        yvdgtkmjbmvhhzm
        xucfsjlialuggyl
        wtberikhzktffxk
        vsadqhjgyjseewj
        urzcpgifxirddvi
        tqybofhewhqccuh
        spxanegdvgpbbtg
        rowzmdfcufoaasf
    """
    return [caesar(msg_encoded, rs, dir='decode') for rs in range(26)]
