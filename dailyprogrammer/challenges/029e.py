#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/r8a70/3222012_challenge_29_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/029e.py

| **Challenge name:** Palindrome (reddit_, source_)
| **Challenge number:** 29
| **Difficulty:** Easy
| **Submission date:** 2012-03-22
| **Status:** Complete

Description
-----------

A `Palindrome <http://en.wikipedia.com/wiki/Palindrome>`_ is a sequence that is the same in
reverse as it is forward.

I.e. hannah, 12321.

Your task is to write a function to determine whether a given string is palindromic or not.

**Bonus**: Support multiple lines in your function to validate Demetri Martin's `224 word palindrome
poem <http://www.pastemagazine.com/articles/2009/02/demetri-martins-palindrome-poem.html>`_.

Thanks to _lerp for submitting this idea in `/r/dailyprogrammer_ideas <http://www.reddit.com/r/dailyprogrammer_ideas>`_!

Example run
-----------

::

    $ python3 dailyprogrammer.py 029e
    Give me a string: hannah
    It's a palindrome!
    Extra: Is the poem 'Dammit I'm Mad' from Demetri Martin a palindrome?
    Yes it is!

Module contents
---------------
"""

from plugins.enhancedstring import EnhancedString


def run():
    """Execute the challenges.029e module."""
    str_ = EnhancedString(input("Give me a string: "))
    options = {True: "It's a palindrome!", False: "Nope, not a palindrome."}
    print(options[str_.is_palindrome()])

    poem = EnhancedString("""Dammit I'm mad.
Evil is a deed as I live.
God, am I reviled? I rise, my bed on a sun, I melt.
To be not one man emanating is sad. I piss.
Alas, it is so late. Who stops to help?
Man, it is hot. I'm in it. I tell.
I am not a devil. I level "Mad Dog".
Ah, say burning is, as a deified gulp,
In my halo of a mired rum tin.
I erase many men. Oh, to be man, a sin.
Is evil in a clam? In a trap?
No. It is open. On it I was stuck.
Rats peed on hope. Elsewhere dips a web.
Be still if I fill its ebb.
Ew, a spider... eh?
We sleep. Oh no!
Deep, stark cuts saw it in one position.
Part animal, can I live? Sin is a name.
Both, one... my names are in it.
Murder? I'm a fool.
A hymn I plug, deified as a sign in ruby ash,
A Goddam level I lived at.
On mail let it in. I'm it.
Oh, sit in ample hot spots. Oh wet!
A loss it is alas (sip). I'd assign it a name.
Name not one bottle minus an ode by me:
"Sir, I deliver. I'm a dog"
Evil is a deed as I live.
Dammit I'm mad.""")
    print("Extra: Is the poem 'Dammit I'm Mad' from Demetri Martin a palindrome?")
    options = {True: "Yes it is!", False: "No it's not... (huh?)"}
    print(options[poem.is_palindrome()])

