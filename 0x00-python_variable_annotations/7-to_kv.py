#!/usr/bin/env python3
""" type-annotated function concat that takes a string str1and
and a string str2 as arguments and returns a concatenated string"""

from typing import Union, Tuple


def to_kv(k: int, v: Union[int, float]) -> Tuple[str, float]:
    """Return concat list of float"""
    return (k, v*2)
