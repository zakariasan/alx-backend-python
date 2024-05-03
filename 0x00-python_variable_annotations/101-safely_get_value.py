#!/usr/bin/env python3
""" type-annotated function concat that takes a string str1and
and a string str2 as arguments and returns a concatenated string"""


from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """ try to get the best of """
    if key in dct:
        return dct[key]
    else:
        return default
