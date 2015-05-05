# authentication - Functions for authenticating users

## Description

This module contains several functions for password management and user authentication.

## Functions

- **random\_password(**l=8**)**

  Generate a random password consisting of `l` characters.

- **hash\_password(**password, salt=None**)**

  Hash the given password after salting with `salt`.

  A salt is randomly generated if none is provided. The returned string is in the format
  `'password_hashed:salt'`.

- **validate\_password(**password, hash\_and\_salt**)**

  Check if `password` matches `hash_and_salt`.

  `hash_and_salt` should be a string of the format `'password_hashed:salt'`. Returns `True`
  if the result of `hash_password(password, salt)` is equal to `hash_and_salt`.
