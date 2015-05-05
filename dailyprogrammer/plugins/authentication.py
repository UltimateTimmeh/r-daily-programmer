#!/usr/bin/python3
"""
Functions for authenticating users
"""

import hashlib
import random
import uuid


def random_password(l=8):
    """Generate a random password consisting of `l` characters."""
    symbols = "ABCDEFGHILJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    symbols += "0123456789<>?!@#$%^&*()_+-=[];{}:"
    password = [random.choice(symbols) for ii in range(l)]
    password = ''.join(password)
    return password


def hash_password(password, salt=None):
    """Hash the given password after salting with `salt`."""
    if salt is None:
        salt = uuid.uuid4().hex
    password_hashed = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    return '{}:{}'.format(password_hashed, salt)


def validate_password(password, hash_and_salt):
    """Check if `password` matches `hash_and_salt`."""
    salt = hash_and_salt.split(':')[-1]
    return hash_password(password, salt) == hash_and_salt
