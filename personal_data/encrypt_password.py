#!/usr/bin/env python3
"""encrypt password module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    returns a salted, hashed password, which is a byte string
    """

    # generate a salt
    salt = bcrypt.gensalt()
    # hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
