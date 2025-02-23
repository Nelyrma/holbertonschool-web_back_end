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

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance based on email and password """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        user_list = []
        try:
            user_list = User.search({"email": user_email})
            if user_list == []:
                return None
        except Exception:
            return None

        user = user_list[0]
        if user.is_valid_password(user_pwd):
            return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the User instance for a request """
        try:
            header = self.authorization_header(request)
            base64_part = self.extract_base64_authorization_header(header)
            clear_part = self.decode_base64_authorization_header(base64_part)
            creadentials = self.extract_user_credentials(clear_part)

            return self.user_object_from_credentials(creadentials[0],
                                                     creadentials[1])
        except Exception:
            return None
