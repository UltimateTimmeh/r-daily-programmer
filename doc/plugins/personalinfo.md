# personalinfo - Storing and handling personal information

## Description

This module contains a class for storing and handling personal information. The PersonalInfo object
is initialized with at least the subject's name and age, but any other imaginable personal data can
be passed as a keyword argument and will then be available in the object as an attribute.

## Classes

### class personalinfo.PersonalInfo(object)

A class for storing and handling personal information.

- *method* **\_\_init\_\_(**name, age, \*\*kwargs**)**

  Initialize the personal information object.

  A PersonalInfo object must be initialized with at least a `name` and
  an `age`. All other keyword arguments are set as attributes.

  Example:

        >>> from personalinfo import PersonalInfo
        >>> pi = PersonalInfo('John Smith', 50, reddit_username='John_Smith')
        >>> print(pi.name); print(pi.age); print(pi.reddit_username)
        John Smith
        50
        John_Smith

- *method* **\_\_str\_\_()**

  Format a string representation of the personal information.

- *method* **write(**fn, mode='a'**)**

  Write the personal information to file `fn`.
