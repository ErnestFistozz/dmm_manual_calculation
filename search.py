from typing import Any


class SearchAlg:
    @staticmethod
    def linear_search(numbers: int, search_target: Any) -> int:
        size = len(numbers)
        for index in range(size):
            if numbers[index] == search_target:
                return index

    @staticmethod
    def binary_search(numbers: list, target: Any) -> int:
        start = 0
        end = len(numbers)-1
        while start <= end:
            mid = start + (end-start)//2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return -1
