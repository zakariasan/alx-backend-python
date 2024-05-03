#!/usr/bin/env python3
""" type-annotated function concat that takes a string str1and
and a string str2 as arguments and returns a concatenated string"""


from typing import List, Any


def zoom_array(lst: List[Any], factor: Any = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
