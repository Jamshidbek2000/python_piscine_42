def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a list of lists.

    Args:
        family: A list of lists.
        start: The start index of the slice.
        end: The end index of the slice.

    Returns:
        A new list that is a slice of the original list.

    Raises:
        TypeError: If `family` is not a list.
        TypeError: If `start` or `end` are not integers.
        ValueError: If `family` is empty.
        ValueError: If `start` is greater than the size of the list.
        ValueError: If `end` is greater than the size of the list.
        ValueError: If `start` is less than 0 and
        `start * (-1)` is greater than the size of the list.
        ValueError: If `end` is less than 0 and
        `end * (-1)` is greater than the size of the list.
        TypeError: If `family` is not a list of lists.
        ValueError: If `family` is not a list of lists of the same size.
    """

    if (type(family) is not list):
        raise TypeError("family must be a list")
    if type(start) is not int or type(end) is not int:
        raise TypeError("start and end must be integers")
    if (len(family) == 0):
        raise ValueError("family is empty")

    sizeOfLists = len(family[0])

    if start > sizeOfLists:
        raise ValueError("start is greater than the size of the list")
    if end > sizeOfLists:
        raise ValueError("end is greater than the size of the list")
    if start < 0 and start * (-1) > sizeOfLists:
        raise ValueError("start is less than 0")
    if end < 0 and end * (-1) > sizeOfLists:
        raise ValueError("end is less than 0")

    for lst in family:
        if type(lst) is not list:
            raise TypeError("family must be a list of lists")
        if (len(lst) != sizeOfLists):
            raise ValueError("family must be a list of lists of the same size")

    result = family[start:end]

    print("The shape is : (%d, %d)" % (len(family), sizeOfLists))
    print("The new shape is : (%d, %d)" % (len(result), sizeOfLists))

    return result


# def test_slice_me():
#     # Test case 1: Valid input, positive start and end
#     family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
#     result = slice_me(family, 0, 2)
#     assert result == [[1.80, 78.4], [2.15, 102.7]], "Test case 1 failed"

#     # Test case 2: Valid input, start is greater than end
#     result = slice_me(family, 2, 0)
#     assert result == [], "Test case 2 failed"

#     # Test case 3: Valid input, negative start and end
#     result = slice_me(family, -2, -1)
#     assert result == [[2.10, 98.5]], "Test case 3 failed"

#     # Test case 4: Invalid input, family is not a list
#     try:
#         slice_me("not_a_list", 0, 2)
#     except TypeError:
#         pass
#     else:
#         assert False, "Test case 4 failed"

#     # Test case 5: Invalid input, start is greater than size of lists
#     try:
#         slice_me(family, 10, 12)
#     except ValueError:
#         pass
#     else:
#         assert False, "Test case 5 failed"

#     # Test case 6: Invalid input, end is greater than size of lists
#     try:
#         slice_me(family, 0, 10)
#     except ValueError:
#         pass
#     else:
#         assert False, "Test case 6 failed"

#     # Add more test cases as needed

#     print("All test cases passed!")


# def main():
#     family = [[1.80, 78.4],
#               [2.15, 102.7],
#               [2.10, 98.5],
#               [1.88, 75.2]]
#     print(slice_me(family, 0, 2))
#     print(slice_me(family, 1, -2))

#     family = [[2.10, 78.45],
#               [4.15, 6.70],
#               [2.10, 98.5],
#               [1.88, 75.2]]
#     print(slice_me(family, 0, 2))
#     print(slice_me(family, 1, -2))

#     test_slice_me()


# if __name__ == "__main__":
#   main()
