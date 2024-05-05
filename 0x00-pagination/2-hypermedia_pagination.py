#!/usr/bin/env python3
"""
Defines the class Server that paginates data from a csv file.
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start index and end index of
    items to fetch based on the page number and page size provided
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "baby.csv"

    def __init__(self):
        """
        Initialize the dataset by None
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the appropriate page of the dataset
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        page_data = self.dataset()
        indexes = index_range(page, page_size)
        print(indexes)
        page_data = page_data[indexes[0]: indexes[1]]

        return page_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a more descriptive response to a request for a page
        (HATEOAS)
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        more_info = {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page != 1 else None,
            'total_pages': total_pages,
        }

        return more_info
