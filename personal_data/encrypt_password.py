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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    verify if the provided password matches the hashed password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
