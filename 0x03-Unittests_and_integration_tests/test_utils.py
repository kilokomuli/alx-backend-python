#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize,
    )
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Defines class that inherits from unittest.TestCase."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map function raises KeyError."""
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(str(err.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Class module for unittest of get_json function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Tests if it returns the expected output."""
        response = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **response)
        mock_get = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """Class module for unittest of memoize function."""
    def test_memoize(self):
        """Method"""

        class TestClass:
            """Wrapper class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
