# Challenge 005 Easy - Password Protect

## Information

**Challenge name:** [Password Protect](http://www.reddit.com/r/dailyprogrammer/comments/pnhyn/2122012_challenge_5_easy/)  
**Challenge number:** 5  
**Difficulty:** Easy  
**Submission date:** 2012-02-13  
**Status:** Complete

## Description

Your challenge for today is to create a program which is password protected, and wont open unless
the correct user and password is given.

For extra credit, have the user and password in a seperate .txt file. For even more extra credit,
break into your own program :).

## Extra credit

Breaking into the program is relatively easy. All that is required to be able to run the "secret\_code"
function is the presence of `user_authenticated` in the challenge module's namespace. The value of this
module variable should be an object that at least has the attribute `username` (which can be whatever,
as long as it can be converted to a string).

    $ python3
    >>> import importlib
    >>> challenge = importlib.import_module('challenges.005e')
    >>> challenge.secret_code()
    ACCESS DENIED! You must first log in. Press ENTER to continue.
    >>> class Dummy(object):
    ...     pass
    ... 
    >>> challenge.user_authenticated = Dummy()
    >>> challenge.user_authenticated.username = 'hacker'
    >>> challenge.secret_code()
    Your username is 'hacker', and you have access to the secret code. Enjoy!
    Press ENTER to continue.
    >>>
