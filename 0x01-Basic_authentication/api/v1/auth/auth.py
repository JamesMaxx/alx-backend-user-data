#!/usr/bin/env python3
"""
Module of Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method for validating if endpoint requires auth

        Args:
            path (str): The path of the endpoint.
            excluded_paths (List[str]): The paths that are excluded from
                authorization.

        Returns:
            bool: True if the endpoint requires auth, False otherwise.
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        l_path = len(path)
        if l_path == 0:
            return True

        slash_path = True if path[l_path - 1] == '/' else False

        tmp_path = path
        if not slash_path:
            tmp_path += '/'

        for exc in excluded_paths:
            l_exc = len(exc)
            if l_exc == 0:
                continue

            if exc[l_exc - 1] != '*':
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[:l_exc - 1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Method that handles authorization header

        Args:
            request (flask.Request): The request object.

        Returns:
            str: The authorization header value.
        """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Validates current user

        Args:
            request (flask.Request): The request object.

        Returns:
            TypeVar('User'): The current user if valid, None otherwise.
        """
        return None
