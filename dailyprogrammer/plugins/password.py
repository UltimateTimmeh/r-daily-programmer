#!/usr/bin/python3
"""
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/plugins/password.py

Create, hash and validate passwords (source_).
"""

import hashlib
import random
import uuid


def random_password(l=8):
    """Generate a random password of arbitrary length.

    The generated password will consist of ``l`` characters that are each randomly
    picked from the collection of alpha-numerical characters (numbers, lower-case
    letters and upper-case letters).

    :param int l: password length (default 8)
    :return: randomly generated password
    :rtype: str

    Example::

        >>> from password import random_password
        >>> random_password()
        'ejKPWSNF'
        >>> random_password(l=20)
        'FgasJS0uUniDGVPraGZk'
    """
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHILJKLMNOPQRSTUVWXYZ"
    pwd = ''.join([random.choice(chars) for ii in range(l)])
    return pwd


def hash_password(pwd, salt=None):
    """Salt and hash a plain text password.

    The provided plain text password ``pwd`` is first salted with ``salt`` and then hashed
    using the SHA256 hashing function. If no ``salt`` is provided, a random one is first
    generated. The returned string is a concatenation of the hashed password and the salt,
    separated with a colon (':').

    :param str pwd: the plain text password to be hashed
    :param salt: the password salt (default None)
    :type salt: str or None
    :return: concatenation of hashed password and salt, separated with a colon
    :rtype: str

    Example::

        >>> from password import hash_password
        >>> hash_password('password')
        'c7ca164ff8952dfef769f75398ebbad20952ee15fd9eae936d823ff57b7ce275:a9192d85fdd2465a9d1dbce823a52d0c'
    """
    if salt is None:
        salt = uuid.uuid4().hex
    pwd_hashed = hashlib.sha256(salt.encode() + pwd.encode()).hexdigest()
    return '{}:{}'.format(pwd_hashed, salt)


def validate_password(pwd, hs):
    """Validate a plain text password by comparing it with the expected hash.

    The string ``hs`` is a concatenation of the expected password hash and the password
    salt, separated with a colon (':'). The plain text password ``pwd`` is hashed with the
    function :func:`plugins.password.hash_password`, the output of which is then compared for
    equality with ``hs``.

    :param str pwd: the plain text password to be tested
    :param str hs: concatenation of the expected password hash and salt, separated with a colon
    :return: True if the password is correct, False if it is not
    :rtype: bool

    Example::

        >>> from password import validate_password
        >>> hs = 'c7ca164ff8952dfef769f75398ebbad20952ee15fd9eae936d823ff57b7ce275:a9192d85fdd2465a9d1dbce823a52d0c'
        >>> validate_password('passwrd', hs)
        False
        >>> validate_password('password', hs)
        True
    """
    salt = hs.split(':')[-1]
    return hash_password(pwd, salt) == hs
