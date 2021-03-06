#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/pnhyn/2122012_challenge_5_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/005e.py

| **Challenge name:** Password Protect (reddit_, source_)
| **Challenge number:** 5
| **Difficulty:** Easy
| **Submission date:** 2012-02-13
| **Status:** Complete

Description
-----------

Your challenge for today is to create a program which is password protected, and wont open unless
the correct user and password is given.

For extra credit, have the user and password in a seperate .txt file. For even more extra credit,
break into your own program :).

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 005e
    === MAIN ===
    1. Log in
    2. Create new user
    3. Look at secret code
    q. Quit
    Choose menu item > 3
    ACCESS DENIED! You must first log in. Press ENTER to continue.
    === MAIN ===
    1. Log in
    2. Create new user
    3. Look at secret code
    q. Quit
    Choose menu item > 2
    New username > johnsmith
    New password (leave blank for random) > password
    Note: Data has been written to file '005e_userdatabase.txt'
    === MAIN ===
    1. Log in
    2. Create new user
    3. Look at secret code
    q. Quit
    Choose menu item > 1
    Username > johnsmith
    Password > password
    Welcome, johnsmith! Press ENTER to continue.
    === MAIN ===
    1. Log in
    2. Create new user
    3. Look at secret code
    q. Quit
    Choose menu item > 3
    You are 'johnsmith', and you have access to the secret code. Enjoy!
    Press ENTER to continue.
    === MAIN ===
    1. Log in
    2. Create new user
    3. Look at secret code
    q. Quit
    Choose menu item > q

Extra credit
------------

Breaking into the program is relatively easy. All that is required to be able to run the
``secret_code`` function is the presence of ``user_authenticated`` in ``challenges.005e``'s
namespace. The value of this variable should be an object that at least has the attribute
``username`` (which can be whatever, as long as it can be converted to a string). To achieve
this, do the following in a terminal::

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

Imported plugins
----------------

| :mod:`plugins.password`
| :mod:`plugins.textmenu`
| :mod:`plugins.user`

Module contents
---------------
"""

import os

from plugins import config as cfg
from plugins import password
from plugins import textmenu
from plugins import user
from plugins import utils

# Set global variables.
user_authenticated = None
userdb_fn = os.path.join(cfg.output_dir, '005e_userdatabase.txt')


# Define functions.
def new_user():
    """Register a new user.

    The user is asked for a username (which has to be unique in the user database)
    and a password. If no password is provided, a random password with a length of
    eight characters is generated. The password is then salted and hashed and the
    user's information is written to the user database file.
    """
    # Ask for new username. Make sure it does not already exist in the database.
    userdb = user.UserDatabase.read(userdb_fn)
    username = utils.get_input("New username > ")
    while userdb.get_users('username', username):
        print("That user already exists, please choose another name.")
        username = utils.get_input("New username > ")

    # Ask for password. Generate random password if left blank.
    pwd = utils.get_input("New password (leave blank for random) > ")
    if pwd == '':
        pwd = password.random_password(l=8)
        print("Your randomly generated password is: {}".format(pwd))
        print("Don't forget it!")

    # Hash the password and add the user to the user database.
    pwd = password.hash_password(pwd)
    userdb.add_user(user.User(username=username, password=pwd))
    userdb.write(userdb_fn)
    print("Note: Data has been written to file '{}'".format(userdb_fn))


def log_in():
    """Log in an existing user.

    The user is asked for a username and password. If the provided username exists
    in the user database and the provided password matches the hash for that user,
    the login is considered successful and ``challenges.005e.user_authenticated`` is
    set to the logged in user.
    """
    global user_authenticated

    # Check if a user is already logged in.
    if user_authenticated is not None:
        print("User '{}' is currently logged in.".format(user_authenticated.username))
        print("Logging in as another user will terminate that session.")

    # Ask for the username and password.
    username = utils.get_input("Username > ")
    pwd = utils.get_input("Password > ")

    # Check if the user exists.
    userdb = user.UserDatabase.read(userdb_fn)
    match = userdb.get_users('username', username)
    if match:
        user_match = match[0]
    else:
        utils.get_input("Incorrect username or password. Press ENTER to continue.")
        return

    # Check if the password is correct.
    if not password.validate_password(pwd, user_match.password):
        utils.get_input("Incorrect username or password. Press ENTER to continue.")
        return

    # Getting here means the provided information is correct. Set authenticated user.User
    user_authenticated = user_match
    utils.get_input("Welcome, {}! Press ENTER to continue.".format(user_authenticated.username))


def secret_code():
    """Code that is only accessible if a user is logged in.

    This function first checks if ``challenges.005e.user_authenticated`` is set to ``None``.
    If this is the case, then no user is logged in and the function stops. If a user is
    logged in, then the function continues and displays the 'secret message'.
    """
    if user_authenticated is None:
        utils.get_input("ACCESS DENIED! You must first log in. Press ENTER to continue.")
        return
    secretmsg = "You are '{}', and you have access to the secret code. Enjoy!"
    print(secretmsg.format(user_authenticated.username))
    utils.get_input("Press ENTER to continue.")


def run():
    """Execute the challenges.005e module."""
    # Create the menus.
    main_menuitems = [
            textmenu.TextMenuItem('1', log_in, 'Log in'),
            textmenu.TextMenuItem('2', new_user, 'Create new user'),
            textmenu.TextMenuItem('3', secret_code, 'Look at secret code'),
            textmenu.TextMenuItem('q', 'quit', 'Quit'),
            ]

    menus = {
        'main_menu': textmenu.TextMenu('MAIN', main_menuitems),
        }

    # Execute the menu engine.
    protectedsoftware = textmenu.TextMenuEngine(menus, 'main_menu')
    protectedsoftware.run()

