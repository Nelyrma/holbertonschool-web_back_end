#!/usr/bin/env python3
""" Module of basic authentification """
from typing import TypeVar
import base64
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """ Basic authentification class """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization header
        for a Basic Authentication
        """
        if (authorization_header is None or
                type(authorization_header) is not str or
                authorization_header[0:6] != "Basic "):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Returns the decoded value of base64_authorization_header """
        if (base64_authorization_header is None or
                type(base64_authorization_header) is not str):
            return None

        try:
            return base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Returns the user email and password from the Base64 decoded value
        """
        if (decoded_base64_authorization_header is None or
                type(decoded_base64_authorization_header) is not str or
                ':' not in decoded_base64_authorization_header):
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password
