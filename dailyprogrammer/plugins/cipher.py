#!/usr/bin/python3
"""
Functions for encoding and decoding messages
"""


def caesar(msg, n, dir='encode'):
    """Encode or decode `msg` using a caesar cipher with a right shift of `n`."""
    # Process arguments.
    msg = msg.lower()
    n = n % 26
    if dir == 'decode':
        n = -n

    # Create cipher map.
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abc_shift = abc[n:] + abc[:n]
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
    """Return all possible options for decoding a caesar-cipher-endoded message."""
    return [caesar(msg_encoded, n, dir='decode') for n in range(26)]
