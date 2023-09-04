def ft_filter(ft, items) -> object:
    """filter(function or None, iterable) --> filter object\n
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    if ft:
        return [item for item in items if ft(item)]
    return [item for item in items if item]
    # filtered_items = []
    # for item in items:
    #     if ft(item) == True:
    #         filtered_items.append(item)
    # return filtered_items

# from filterstring import ft_filter


# copy = ft_filter.__doc__
# original = filter.__doc__

# print(copy)
# # output: docstring
# print(original == copy)
# # output: True


# def is_odd(number) -> bool:
#     return number % 2 == 1


# def is_even(number) -> bool:
#     return number % 2 == 0


# def test():
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#     print(ft_filter(is_odd, numbers))
#     print(ft_filter(is_even, numbers))
