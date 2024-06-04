#!/usr/bin/env python3
"""
This module defines the User class that represents a user in the API.
"""
import hashlib
from models.base import Base


class User(Base):
    """
    User class that represents a user in the API.

    Attributes:
        email (str): The user's email address.
        _password (str): The user's password hashed with SHA256.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
        Initialize a User instance.

        Args:
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email')
        self._password = kwargs.get('_password')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')

    @property
    def password(self) -> str:
        """
        Getter of the password.
        """
        return self._password

    @password.setter
    def password(self, pwd: str):
        """
        Setter of a new password: encrypt in SHA256.

        Args:
            pwd (str): The new password.
        """
        if pwd is None or not isinstance(pwd, str):
            self._password = None
        else:
            self._password = hashlib.sha256(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd: str) -> bool:
        """
        Validate a password.

        Args:
            pwd (str): The password to validate.

        Returns:
            bool: True if the password is valid, False otherwise.
        """
        if pwd is None or not isinstance(pwd, str):
            return False
        if self.password is None:
            return False
        pwd_e = pwd.encode()
        return hashlib.sha256(pwd_e).hexdigest().lower() == self.password

    def display_name(self) -> str:
        """
        Display User name based on email/first_name/last_name.

        Returns:
            str: The user's display name.
        """
        if self.email is None and self.first_name is None \
                and self.last_name is None:
            return ""
        if self.first_name is None and self.last_name is None:
            return "{}".format(self.email)
        if self.last_name is None:
            return "{}".format(self.first_name)
        if self.first_name is None:
            return "{}".format(self.last_name)
        else:
            return "{} {}".format(self.first_name, self.last_name)
