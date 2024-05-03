#!/usr/bin/env python3
""" type-annotated function concat that takes a string str1and
and a string str2 as arguments and returns a concatenated string"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return concat list of float"""

    def mult(y: float) -> float:
        """multi func"""
        return y * multiplier
    return mult
