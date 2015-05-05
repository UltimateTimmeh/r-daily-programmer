# personalinfo - Storing and handling a user's information

## Description

This module contains a class for storing and handling information about a user. The User object
is initialized with at least the subject's name and age, but any other imaginable info can
be passed as a keyword argument and will then be available in the object as an attribute.

## Classes

### class user.User(object)

A class for storing and handling a user's information.

- *method* **\_\_init\_\_(**name, age, \*\*kwargs**)**

  Initialize the user object.

  A User object must be initialized with at least a `name` and
  an `age`. All other keyword arguments are set as attributes.

  Example:

        $ python3
        >>> from personalinfo import PersonalInfo
        >>> pi = PersonalInfo('John Smith', 50, reddit_username='John_Smith')
        >>> print(pi.name); print(pi.age); print(pi.reddit_username)
        John Smith
        50
        John_Smith

- *method* **\_\_str\_\_()**

  Format a string representation of the user.

- *method* **\_\_eq\_\_(**other**)**

  Test if User object `self` is equal to User object `other`.

  Returns `True` if `other` is a User object *and* the attribute dictionaries
  of `self` and `other` are equal.

- *method* **write(**fn, mode='a'**)**

  Write the user's information to file `fn`.

### class user.UserDatabase(object)

A class for managing a collection of users.

- *class variable* **attrs_extra**

  The extra attributes each User object in the UserDatabase object should have on top of
  the default 'name' and 'age' attributes.

- *method* **\_\_init\_\_(**users**)**

  Initialize the UserDatabase object.

  `users` should be a list of valid User objects (see static method `is_valid_user`).

- *method* **add_user(**user**)**

  Add `user` to the UserDatabase.

  Only adds `user` to the list of users if it is valid (see static method `is_valid_user`).

- *method* **get_users(**attr, val**)**

  Return the list of users that have `val` as the value for attribute `attr`.

- *method* **write(**fn**)**

  Write the contents of the UserDatabase object to file `fn`.

  The first line of the file will be the header, stating the attributes of the User objects.
  The following lines are the values of those attributes for all User objects in the
  UserDatabase. Each attribute/value in a line is separated with a semicolon (`;`) character.

- *classmethod* **read(**fn**)**

  Load the contents of user database file `fn` as a UserDatabase object.

  If file `fn` does not exist, a UserDatabase object with empty user list is returned.
  Otherwise the file is loaded. If the header or one of the datalines in the file are
  invalid, a `ValueError` is raised.

- *staticmethod* **is\_valid\_user(**user**)**

  Check if `user` is a valid entry for the UserDatabase object.

  Checks if `user` is a User object and if it has all extra attributes that are required
  (see class variable `attrs_extra`).
