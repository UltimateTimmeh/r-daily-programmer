#!/usr/bin/python3
"""
Main execution script for challenge '003Easy - Caesar Cipher'.
"""

from plugins import cipher


def run():
    # Ask for input
    msg = input("Message to encode > ")
    n = int(input("Amount of right shift > "))

    # Play with the input
    print("Original message: " + msg)
    msg_encoded = cipher.caesar(msg, n)
    print("Encoded message: " + msg_encoded)
    msg_decoded = cipher.caesar(msg_encoded, n, dir='decode')
    print("Decoded encoded message: " + msg_decoded)
    options = cipher.caesar_brute_force(msg_encoded)
    print("Brute-force-decoded encoded message:")
    print('\n'.join(options))
