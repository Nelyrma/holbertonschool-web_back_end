#!/usr/bin/env python3
""" Module of authentification """
from typing import List
from flask import request


class Auth():
    """ Authentication class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return True if the path is not in
        the list of strings excluded_path
        """
        if not path or not excluded_paths or excluded_paths == []:
            return True
        if path[-1] == "/":
            path = path[:-1]
        for i in range(len(excluded_paths)):
            if excluded_paths[i][-1] == "/":
                excluded_paths[i] = excluded_paths[i][:-1]
            if excluded_paths[i][-1] == "*":
                len_excl_path = len(excluded_paths[i][:-1])
                if path[:len_excl_path] == excluded_paths[i][:len_excl_path]:
                    return False
        if path in excluded_paths:
            return False
        return True
