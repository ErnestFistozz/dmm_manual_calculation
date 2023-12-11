from typing import Any


class SearchAlg:
    @staticmethod
    def linear_search(numbers: int, search_target: Any) -> int:
        '''
            linear search algorithm
        '''
        if not numbers:
            return -1
        if not isinstance(search_target, int) or not all(isinstance(num, int) for num in numbers):
            raise TypeError(
                "Search target and list must be an of type integers")

        size = len(numbers)
        for index in range(size):
            if numbers[index] == search_target:
                return index
        return -1

    @staticmethod
    def binary_search(numbers: list, target: Any) -> int:
        '''
            binary search algorithm
        '''
        if not numbers:
            return -1
        if not isinstance(target, int) or not all(isinstance(num, int) for num in numbers):
            raise TypeError("Search target and list must be integers")

        start = 0
        end = len(numbers)-1
        sorted(numbers)  # enure to sort the array before searching

        while start <= end:
            mid = start + (end-start)//2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return -1
