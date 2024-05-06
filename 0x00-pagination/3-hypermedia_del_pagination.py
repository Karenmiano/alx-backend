#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return data of length page_size
        """
        dataset = self.indexed_dataset()
        len_dataset = len(dataset)
        start = None
        if index in dataset:
            start = index
        else:
            for i in range(index + 1, len_dataset):
                if i in dataset:
                    start = i
                    break

        if start is None:
            raise AssertionError
        start, end = start, start + page_size
        data = []
        for i in range(start, end):
            if dataset.get(i):
                data.append(dataset[i])

        return {
            'index': index,
            'data': data,
            'next_index': end,
            'page_size': len(data),
        }
