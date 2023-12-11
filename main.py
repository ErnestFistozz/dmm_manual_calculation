from search import SearchAlg
from sort import SortAlg


if __name__ == '__main__':
    nums = [1, 2, 3, -4, 5, 8, -6, 7, -1, 9]
    result = SearchAlg.binary_search(nums, 8)
    print(result)

    arr = [1, 2, 3, -4, 5, 8, -6, 7, -1, 9]
    SortAlg.insertion_sort(arr)
    print(arr)
