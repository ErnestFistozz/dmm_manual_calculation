from typing import Any


class SortAlg:

    @staticmethod
    def bubble_sort(numbers: int) -> None:
        n = len(numbers)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return

    @staticmethod
    def insertion_sort(array):
        for i in range(1, len(array)):
            key_item = array[i]
            j = i - 1
            while j >= 0 and array[j] > key_item:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key_item
        return
