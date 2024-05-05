#!/usr/bin/env python3
"""
Class Server
"""
import csv
import math
from typing import List, Tuple, Dict
from math import ceil


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Constructor
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get page content
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        _range = index_range(page, page_size)
        _start = _range[0]
        _end = _range[1]
        return self.dataset()[_start:_end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Hypermedia pagination
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        _range = index_range(page, page_size)
        _start = _range[0]
        _end = _range[1]
        _dataPage = self.get_page(page, page_size)
        _dataFull = self.dataset()
        _total_pages = ceil(len(_dataFull) / page_size)

        _dict = {
            "page_size": len(_dataPage),
            "page": page,
            "data": _dataPage,
            "next_page": page + 1 if page < _total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": _total_pages
        }
        return _dict
