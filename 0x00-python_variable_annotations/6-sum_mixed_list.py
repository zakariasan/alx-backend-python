#!/usr/bin/env python3
""" type-annotated function concat that takes a string str1and
and a string str2 as arguments and returns a concatenated string"""

from typing import List


def sum_mixed_list(mxd_lst: List[float, int]) -> float:
    """Return concat list of float"""
    return sum(mxd_lst)
