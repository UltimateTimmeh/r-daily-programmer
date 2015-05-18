#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/pkw2m/2112012_challenge_3_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/003e.py

| **Challenge name:** Caesar Cipher (reddit_, source_)
| **Challenge number:** 3
| **Difficulty:** Easy
| **Submission date:** 2012-02-11
| **Status:** Complete

Description
-----------

Welcome to cipher day!

Write a program that can encrypt texts with an alphabetical caesar cipher. This cipher can ignore
numbers, symbols, and whitespace.

For extra credit, add a "decrypt" function to your program!

Example run
-----------

::

    $ python3 dailyprogrammer.py 003e
    Message to encode > dailyprogrammer
    Amount of right shift > 5
    Original message: dailyprogrammer
    Encoded message: ifnqduwtlwfrrjw
    Decoded encoded message: dailyprogrammer
    Brute-force-decoded encoded message:
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
    qnvylcebtenzzre
    pmuxkbdasdmyyqd
    oltwjaczrclxxpc
    nksvizbyqbkwwob
    mjruhyaxpajvvna
    liqtgxzwoziuumz
    khpsfwyvnyhttly
    jgorevxumxgsskx

Module contents
---------------
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


def run():
    """Execute the challenges.003e module."""
    # Ask for input
    msg = input("Message to encode > ")
    n = int(input("Amount of right shift > "))

    # Play with the input
    print("Original message: " + msg)
    msg_encoded = caesar(msg, n)
    print("Encoded message: " + msg_encoded)
    msg_decoded = caesar(msg_encoded, n, dir='decode')
    print("Decoded encoded message: " + msg_decoded)
    options = caesar_brute_force(msg_encoded)
    print("Brute-force-decoded encoded message:")
    print('\n'.join(options))
