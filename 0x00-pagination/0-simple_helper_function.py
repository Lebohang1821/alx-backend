#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_range function
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
