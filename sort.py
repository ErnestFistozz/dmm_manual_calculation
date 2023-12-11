from typing import Any


class SortAlg:
    @staticmethod
    def bubble_sort(numbers: list) -> None:
        '''
            bubble sort algorithm
        '''
        if not numbers or not all(isinstance(num, int) for num in numbers):
            return
        n = len(numbers)
        isswaped: bool = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if numbers[j] > numbers[j + 1]:
                    isswaped = True
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            if not isswaped:
                return  # list is already sorted
        return

    @staticmethod
    def insertion_sort(numbers: list) -> None:
        '''
            insertion sort algorithm
        '''
        for i in range(1, len(numbers)):
            key_item = numbers[i]
            j = i - 1
            while j >= 0 and numbers[j] > key_item:
                numbers[j + 1] = numbers[j]
                j -= 1
            numbers[j + 1] = key_item
        return
