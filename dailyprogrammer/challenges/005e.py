#!/usr/bin/python3
"""
Main execution script for challenge '005Easy - Password Protect'.
"""

import os

from plugins import config as cfg
from plugins import textmenu, user, authentication

# Set global variables.
user_authenticated = None
userdb_fn = os.path.join(cfg.output_dir, '005e_userdatabase.txt')


# Define functions.
def new_user():
    """Ask for new username and password and add to the user database."""
    # Ask for new username. Make sure it does not already exist in the database.
    userdb = user.UserDatabase.read(userdb_fn)
    username = input("New username > ")
    while len(userdb.get_users('username', username)) >= 1:
        print("That user already exists, please choose another name.")
        username = input("New username > ")

    # Ask for password. Generate random password if left blank.
    password = input("New password (leave blank for random) > ")
    if password == '':
        password = authentication.random_password(l=8)
        print("Your randomly generated password is: {}".format(password))
        print("Don't forget it!")

    # Ask some additional personal information.
    name = input("Name > ")
    age = int(input("Age > "))

    # Hash the password and add the user to the user database.
    password = authentication.hash_password(password)
    userdb.add_user(user.User(name, age, username=username, password=password))
    userdb.write(userdb_fn)


def log_in():
    """Ask for existing username and password and attempt to log in."""
    global user_authenticated

    # Check if a user is already logged in.
    if user_authenticated is not None:
        print("User '{}' is currently logged in.".format(user_authenticated.username))
        print("Logging in as another user will terminate that session.")

    # Ask for the username and password.
    username = input("Username > ")
    password = input("Password > ")

    # Check if the user exists.
    userdb = user.UserDatabase.read(userdb_fn)
    match = userdb.get_users('username', username)
    if match:
        user_match = match[0]
    else:
        input("Incorrect username or password. Press ENTER to continue.")
        return

    # Check if the password is correct.
    if not authentication.validate_password(password, user_match.password):
        input("Incorrect username or password. Press ENTER to continue.")
        return

    # Getting here means the provided information is correct. Set authenticated user.User
    user_authenticated = user_match
    input("Welcome, {}! Press ENTER to continue.".format(user_authenticated.name))


def secret_code():
    """Code that is only accessible if a user is logged in."""
    if user_authenticated is None:
        input("ACCESS DENIED! You must first log in. Press ENTER to continue.")
        return
    secretmsg = "Your username is '{}', and you have access to the secret code. Enjoy!"
    print(secretmsg.format(user_authenticated.username))
    input("Press ENTER to continue.")


def run():
    # Create the menus.
    main_menuitems = [
            ['1', 'Log in', log_in],
            ['2', 'Create new user', new_user],
            ['3', 'Look at secret code', secret_code],
            ['q', 'Quit', 'quit'],
            ]

    menus = {
        'main_menu': textmenu.TextMenu('MAIN', main_menuitems),
        }

    # Execute the menu engine.
    protectedsoftware = textmenu.TextMenuEngine(menus, main='main_menu')
    protectedsoftware.run()
