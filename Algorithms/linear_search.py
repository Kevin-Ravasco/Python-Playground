"""
This file covers the linear search algorithm with an example.
Has a big O notation of O(n).
"""


def linear_search(arr, x):
    if type(arr) != list:
        return 'The first argument should be a list'

    if x not in arr:
        return 'X not in the list'

    for i in arr:
        if i == x:
            return arr.index(i)


my_array = [2, 3, 8, 9, 4, 6, 7, 5, 1]

# my_dict = {'j': 5, 'k': 4, 'l': 9}

ans = linear_search(my_array, 4)

print(ans)
