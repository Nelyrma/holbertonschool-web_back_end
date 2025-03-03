#!/usr/bin/env python3
"""parameterize a unit test
"""
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        """test that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
