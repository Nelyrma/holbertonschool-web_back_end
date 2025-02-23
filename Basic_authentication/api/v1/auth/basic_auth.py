#!/usr/bin/env python3
""" Module of basic authentification """
from typing import TypeVar
import base64
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """ Basic authentification class """
    def decode_base64_authorization_header(
        self, base64_authorization_header: str) -> str:
        """ Returns the decoded value of base64_authorization_header """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            # Decode the Base64 string
            decoded_bytes = base64.b64decode(base64_authorization_header)
            # Convert bytes to UTF-8 string
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except Exception:
            return None
