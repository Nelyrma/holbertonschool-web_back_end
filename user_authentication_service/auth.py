#!/usr/bin/env python3
"""Hash password module
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """hash a password with bcrypt"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed
