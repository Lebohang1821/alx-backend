#!/usr/bin/env python3
"""
Helper function for pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    It calculates start and end index for pagination
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
