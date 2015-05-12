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

from plugins import cipher


def run():
    """Execute the challenges.003e module."""
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
