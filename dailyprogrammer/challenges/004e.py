#!/usr/bin/python3
"""
Main execution script for challenge '004Easy - Random Password'.
"""

from plugins import authentication


def run():
    # Ask for input.
    np = int(input("Amount of passwords > "))
    lp = int(input("Password length > "))

    # Generate the passwords.
    passwords = [authentication.random_password(l=lp) for ii in range(np)]
    print("===PASSWORDS===")
    print('\n'.join(["{}. {}".format(pi+1, password) for pi, password in enumerate(passwords)]))
    print("="*15)
