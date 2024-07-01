#!/usr/bin/env python3
"""Familiarize yourself with the utils.access_nested_map function and
understand its purpose. Play with it in the Python console to make
sure you understand.

In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that
the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for
ollowing inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
"""

import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
from typing import Mapping, Tuple, Union, Type, Dict
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Tuple[str],
                               expected: Union[Mapping, int]) -> None:
        """_summary_
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Tuple[str],
                                         expected: Type[Exception]) -> None:
        """_summary_
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    _summary_
    Args:
                    unittest (_type_): _description_
    """
    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
    )
    def test_get_json(self, test_url: str, test_payload:
                      Dict[str, bool]) -> None:
        """
        _summart_
        """
        with patch("utils.requests.get") as mock:
            mock.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)

            mock.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    _summary_
    Args:
                    unittest (_type_): _description_
    """
    def test_memoize(self):
        """_summary_

        Returns:
                _type_: _description_
        """
        class TestClass:
            """
            _summary_
            """

            def a_method(self):
                """_summary_

                Returns:
                        _type_: _description_
                """
                return 42

            @memoize
            def a_property(self):
                """_summary_

                Returns:
                        _type_: _description_
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as a_mocked:
            test = TestClass()
            test.a_property
            test.a_property
            a_mocked.assert_called_once()
