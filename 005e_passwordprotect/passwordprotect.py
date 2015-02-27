"""
Fun little program to practice user creation and login. Applies salting and
hashing to make the user database as secure as possible.
"""

import hashlib as hl
import menu
import pwgenerate
import uuid


def existing_user(username):
    """Check if username is an existing user."""
    with open('user_database.txt', 'r') as db_file:
        db_lines = db_file.readlines()
    users = [line.split()[0] for line in db_lines]
    return username in users


def add_user(username, password):
    """Add a user to the database."""
    salt = uuid.uuid4().hex
    hashed_password = hl.sha256(salt.encode() + password.encode()).hexdigest()
    db_entry = username + ' ' + salt + ' ' + hashed_password
    with open('user_database.txt', 'a') as db_file:
        db_file.write(db_entry + '\n')


def get_user(username):
    """Extract a user's salt and hashed password from the database."""
    with open('user_database.txt', 'r') as db_file:
        db_lines = [line.split() for line in db_file.readlines()]
    users = [line[0] for line in db_lines]
    ui = users.index(username)
    salt = db_lines[ui][1]
    hashed_password = db_lines[ui][2]
    return salt, hashed_password


def user_creation():
    """Create a new user. Provide random password if none is provided."""
    # Ask new username, make sure it does not already exist.
    username = input("New username: ")
    while existing_user(username):
        print("That user already exists, please choose another name.")
        username = input("New user name: ")
        
    # Ask new password, generate random if left blank.
    password = input("New password (leave blank for random): ")
    if password == '':
        password = pwgenerate.generate_passwords(1, 8)[0]
        print("Your randomly generated password is: {}".format(password))
    
    # Add user to database.
    add_user(username, password)
    input("User successfully created! Press ENTER to continue.")


def user_identification():
    """Ask for username and password. Identify if they are correct."""
    global user
    
    # Check if you are already logged in.
    if user is not None:
        print("You are already logged in as '{}'!".format(user))
        print("Logging in as another user will log out that session.")
    
    # Ask for username and password.
    username = input("Username: ")
    password = input("Password: ")
    
    # Make sure the user exists. If he does, get his data.
    if not existing_user(username):
        input("Incorrect username or password. Press ENTER to continue.")
        return
    
    # Compare the provided password with the hash in the database.
    salt, hashed_password = get_user(username)
    if hashed_password != hl.sha256(salt.encode() + password.encode()).hexdigest():
        input("Incorrect username or password. Press ENTER to continue.")
        return
    
    # Getting here means the login was successful. Set the user.
    user = username
    input("Login successful! Press ENTER to continue.")


def protected_code():
    """This code can only be executed if a user is logged in."""
    if user is None:
        input("ACCESS DENIED! You must first log in. Press ENTER to continue.")
        return
    print("You are '{}', and you have access to the secret code.".format(user))
    print("Here it is:")
    print("=====")
    print(uuid.uuid4().hex)
    print("=====")
    input("Don't tell anyone! Press ENTER to continue.")


if __name__ == '__main__':
    user = None
    main_menuitems = [
        ['1', 'Log in', user_identification],
        ['2', 'Create new user', user_creation],
        ['3', 'Look at secret code', protected_code],
        ['q', 'Quit', 'quit'],
        ]
    main_menu = menu.TextMenu('MAIN MENU', main_menuitems)
    main_menu.ask_item()


# End
