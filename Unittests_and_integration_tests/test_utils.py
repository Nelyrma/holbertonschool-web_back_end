#!/usr/bin/env python3
"""test_utils module
"""
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """test that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test that a KeyError is raised"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(expected, str(error.exception))
