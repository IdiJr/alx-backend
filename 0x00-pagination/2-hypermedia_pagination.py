#!/usr/bin/env python3
"""
Module with a helper function for pagination and a Server class
"""

import csv
from math import ceil
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names. """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Initialize instance. """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Output page of dataset based on the given
        pagination parameters.
        Args:
            page (int): The current page number.
            page_size (int): The number of items per page.
        Returns:
            List[List]: A list of rows corresponding to the
            requested page.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        # Calculate start and end indexes using index_range function
        start_index, end_index = index_range(page, page_size)

        # Return the appropriate page of the dataset
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Return a dictionary containing information about the dataset page
        and pagination details.
        Args:
            page (int): The current page number.
            page_size (int): The number of items per page.
        Returns:
            dict: A dictionary containing pagination details.
            page_size - length of dataset page
                page - current page number
                data - dataset page
                next_page - number of next page if there is one
                prev_page - number of previous page if there is one
                total_pages - total number of pages
        """

        # Get the dataset page using the get_page method
        data_page = self.get_page(page, page_size)

        # Calculate start and end indexes for the current page
        start_index, end_index = index_range(page, page_size)

        # Calculate total pages in the dataset
        total_pages = ceil(len(self.dataset()) / page_size)

        # Calculate next and previous pages
        next_page = page + 1 if end_index < len(self.dataset()) else None
        prev_page = page - 1 if start_index > 0 else None

        # Return the dictionary with pagination details
        return {
            'page_size': len(data_page),
            'page': page,
            'data': data_page,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
