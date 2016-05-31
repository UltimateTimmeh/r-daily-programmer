#!/usr/bin/python3
"""
Information
-----------

.. _reddit: https://www.reddit.com/r/dailyprogrammer/comments/t33vi/522012_challenge_47_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/047e.py

| **Challenge name:** Caesar Cipher 2 (reddit_, source_)
| **Challenge number:** 47
| **Difficulty:** Easy
| **Submission date:** 2012-05-02
| **Status:** Complete

Description
-----------

Your task today is to implement one of the oldest ciphers known, the so-called
`Caesar cipher <http://en.wikipedia.org/wiki/Caesar_cipher>`_ (or *Caesar shift*, as it is sometimes
called). It works like this: for every letter you want to encrypt, you shift it some number of
places down the alphabet to get the letter in the cipher.

So, for instance, in a Caesar cipher with a shift of 3, "A" becomes "D", "B" becomes "E", "C"
becomes "F", and so on. At the end of the alphabet it wraps around, so "W" becomes "Z", "X" becomes
"A", "Y" becomes "B" and "Z" becomes "C". If you encrypt "Hello" with a shift of 3, you get "Khoor".

One interesting thing about this cipher is that you can use the same algorithm to decode a cipher
as you can to encode it: if you wish to decrypt some text that has been Caesar-shifted 6 places, you
simply shift it another 20 places to get back the original text. For example, if you encrypt
"Daily programmer"  with a shift of 6 you get "Jgore vxumxgsskx", and if you encrypt "Jgore
vxumxgsskx" with a shift of 20 you get "Daily programmer".

Implement the cipher and encrypt a bit of text of your choice!

**Bonus**

Using your program, become a code-cracker and decrypt this cipher (posted in honor of Mayday)::

    Spzalu - zayhunl dvtlu sfpun pu wvukz kpzaypibapun zdvykz pz uv ihzpz mvy h
    zfzalt vm nvclyutlua.  Zbwyltl leljbapcl wvdly klypclz myvt h thukhal myvt aol
    thzzlz, uva myvt zvtl mhyjpjhs hxbhapj jlyltvuf. Fvb jhu'a lewlja av dplsk
    zbwyltl leljbapcl wvdly qbza 'jhbzl zvtl dhalyf ahya aoyld h zdvyk ha fvb! P
    tlhu, pm P dlua hyvbuk zhfpu' P dhz hu ltwlylyvy qbza iljhbzl zvtl tvpzalulk
    ipua ohk sviilk h zjptpahy ha tl aolf'k wba tl hdhf!... Ho, huk uvd dl zll aol
    cpvslujl puolylua pu aol zfzalt! Jvtl zll aol cpvslujl puolylua pu aol zfzalt!
    Olsw! Olsw! P't ilpun ylwylzzlk!

Thanks to `/u/frenulem <https://www.reddit.com/user/frenulem>`_ for posting this idea on
`/r/dailyprogrammer_ideas <https://www.reddit.com/r/dailyprogrammer_ideas>`_! If you have a problem
that you think would be good for us, head over there and contribute!

Example run
-----------

.. note:: This challenge is pretty much identical to `003e - Caesar Cipher <challenges.003e.html>`_.
          Because I don't think that code deserves its own plugin (at least not until some more
          interesting cipher challenge pops up), I have decided to simply import the other challenge
          module.

::

    First I use brute force to decode the first word:

    spzalu
    royzkt
    qnxyjs
    pmwxir
    olvwhq
    nkuvgp
    mjtufo
    listen
    khrsdm
    jgqrcl
    ifpqbk
    heopaj
    gdnozi
    fcmnyh
    eblmxg
    daklwf
    czjkve
    byijud
    axhitc
    zwghsb
    yvfgra
    xuefqz
    wtdepy
    vscdox
    urbcnw
    tqabmv

    Looking at the different options, I believe 'listen' is the only one that makes
    sense. This word is eighth in the list, meaning the message was encoded with a
    shift of 7. So now just apply that to the whole message:

    listen - strange women lying in ponds distributing swords is no basis for a
    system of government.  supreme executive power derives from a mandate from the
    masses, not from some farcical aquatic ceremony. you can't expect to wield
    supreme executive power just 'cause some watery tart threw a sword at you! i
    mean, if i went around sayin' i was an empereror just because some moistened
    bint had lobbed a scimitar at me they'd put me away!... ah, and now we see the
    violence inherent in the system! come see the violence inherent in the system!
    help! help! i'm being repressed!

Imported plugins
----------------

| None

Module contents
---------------
"""

import importlib as il
import os

from plugins import config as cfg
cc = il.import_module('challenges.003e')


def run():
    """Execute the challenges.047e module."""
    input_fp = os.path.join(cfg.input_dir, '047e_example_input.txt')
    with open(input_fp, 'r') as input_file:
        text = input_file.read()
    print("First I use brute force to decode the first word:", end='\n\n')
    print('\n'.join(cc.caesar_brute_force(text.split()[0])), end='\n\n')
    print("Looking at the different options, I believe 'listen' is the only one that makes")
    print("sense. This word is eighth in the list, meaning the message was encoded with a")
    print("shift of 7. So now just apply that to the whole message:", end='\n\n')
    print(cc.caesar(text, 7, dir='decode'))

