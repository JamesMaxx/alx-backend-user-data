#!/usr/bin/env python3
"""
Module of Basic Authentication

This module implements the BasicAuth class, which is a subclass of the
Auth class. It provides methods for extracting user credentials, decoding
base64 authorization headers, and retrieving the User instance for a request.

"""

from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User


class BasicAuth(Auth):
    """
    Basic Authentication Class

    This class extends the Auth class and provides methods for extracting
    user credentials, decoding base64 authorization headers, and retrieving
    the User instance for a request.

    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extract Base 64 Authorization Header

        This method extracts the base64 encoded authorization header from the
        provided authorization header.

        Args:
            authorization_header (str): The authorization header.

        Returns:
            str: The extracted base64 encoded authorization header, or None if
                 the header is invalid.

        """
        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        encoded = authorization_header.split(' ', 1)[1]

        return encoded

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        Decode the value of a base64 string

        This method decodes the base64 encoded authorization header.

        Args:
            base64_authorization_header (str): The base64 encoded authorization
                                               header.

        Returns:
            str: The decoded authorization header, or None if the decoding fails.

        """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None

        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = b64decode(encoded)
            decoded = decoded64.decode('utf-8')
        except BaseException:
            return None

        return decoded

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        Extract user credentials from the base64 decoded value

        This method extracts the user email and password from the base64
        decoded authorization header.

        Args:
            decoded_base64_authorization_header (str): The base64 decoded
                                                       authorization header.

        Returns:
            tuple: A tuple containing the user email and password, or None if
                   the header is invalid.

        """
        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(':', 1)

        return credentials[0], credentials[1]

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> User:
        """
        Retrieve the User instance based on user credentials

        This method retrieves the User instance based on the provided user
        email and password.

        Args:
            user_email (str): The user email.
            user_pwd (str): The user password.

        Returns:
            User: The User instance, or None if the credentials are invalid.

        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            found_users = User.search({'email': user_email})
        except Exception:
            return None

        for user in found_users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> User:
        """
        Retrieve the User instance for a request

        This method retrieves the User instance for the provided request by
        extracting the user credentials from the request headers and retrieving
        the User instance based on the credentials.

        Args:
            request (flask.Request, optional): The request object.

        Returns:
            User: The User instance, or None if the credentials are invalid.

        """
        auth_header = self.authorization_header(request)

        if not auth_header:
            return None

        encoded = self.extract_base64_authorization_header(auth_header)

        if not encoded:
            return None

        decoded = self.decode_base64_authorization_header(encoded)

        if not decoded:
            return None

        email, pwd = self.extract_user_credentials(decoded)

        if not email or not pwd:
            return None

        user = self.user_object_from_credentials(email, pwd)

        return user
