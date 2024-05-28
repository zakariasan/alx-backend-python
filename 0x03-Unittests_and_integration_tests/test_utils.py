#!/usr/bin/env python3
""" test utils python3 """

import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """ test access nested Map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test access nested map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ test map exception """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(path[-1]))


class TestGetJson(unittest.TestCase):
    """ test get json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ test get json """
        with patch('requests.get') as mocked_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mocked_get.return_value = mock_response
            result = get_json(test_url)
            mocked_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ test memoize """
    class TestClass:
        """ test class """

        def a_method(self):
            """ a_method """
            return 42

        @memoize
        def a_property(self):
            """ a_property """
            return self.a_method()

    def test_memoize(self):
        """ test memoize """
        test_instance = self.TestClass()
        with patch.object(self.TestClass,
                          'a_method',
                          return_value=42) as mock_method:
            result1 = test_instance.a_property
            result2 = test_instance.a_property
            mock_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
