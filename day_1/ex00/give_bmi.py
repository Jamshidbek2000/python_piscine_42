def only_int_or_float(lst: list[int | float]) -> bool:
    """
    Checks if all elements in the list are integers or floats.

    Args:
        lst: A list of integers or floats.

    Returns:
        True if all elements in the list are integers or floats,
        False otherwise.
    """

    for i in lst:
        if not isinstance(i, int) and not isinstance(i, float):
            return False
    return True


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculates the BMI for a list of heights and weights.

    Args:
        height: A list of heights.
        weight: A list of weights.

    Returns:
        A list of BMIs.

    Raises:
        AssertionError: If `height` or `weight` is not a list.
        AssertionError: If the lengths of `height` and `weight` are not equal.
        AssertionError: If any element in `height` or `weight` is
        not an int or float.
    """

    if type(height) is not list or type(weight) is not list:
        raise AssertionError("bad input")
    if len(height) == 0 or len(height) != len(weight):
        raise AssertionError("bad input")
    if not only_int_or_float(height) or not only_int_or_float(weight):
        raise AssertionError("bad input")

    bmi = []
    for i in range(len(height)):
        bmi.append(weight[i] / (height[i] * height[i]))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks if the BMIs in a list are above a certain limit.

    Args:
        bmi: A list of BMIs.
        limit: The BMI limit.

    Returns:
        A list of booleans,
        indicating whether the corresponding BMI is above the limit.

    Raises:
        AssertionError: If `bmi` is not a list.
        AssertionError: If any element in `bmi` is not an integer or float.
    """

    if not only_int_or_float(bmi):
        raise AssertionError("bad input")

    results = []
    for i in range(len(bmi)):
        if bmi[i] > limit:
            results.append(True)
        else:
            results.append(False)
    return results


# def my_test():

#     height1 = [2, 1.15, 1.65, 1.95, 1.90]
#     weight1 = [165.3, 38.4, 62.2, 92, 73]

#     height2 = [2, 1.15, 1.65, 1.95, 1.90, 'hello']
#     weight2 = [165.3, 38.4, 62.2, 92, 73, 'world']

#     height3 = [2, 1.15, 1.65, 1.95, 1.90, 1.64]
#     weight3 = [165.3, 38.4, 62.2, 92, 73]

#     height4 = []
#     weight4 = [165.3, 38.4, 62.2, 92, 73]

#     height5 = 1
#     weight5 = 'hello'

#     print("\n\nExample 1")
#     try:
#         bmi = give_bmi(height1, weight1)
#         print(bmi)

#         limits = apply_limit(bmi, 25)
#         print(limits)
#     except Exception as e:
#         print("Error:", e)

#     print("\n\nExample 2")
#     try:
#         bmi = give_bmi(height2, weight2)
#         print(bmi)

#         limits = apply_limit(bmi, 25)
#         print(limits)
#     except Exception as e:
#         print("Error:", e)

#     print("\n\nExample 3")
#     try:
#         bmi = give_bmi(height3, weight3)
#         print(bmi)

#         limits = apply_limit(bmi, 25)
#         print(limits)
#     except Exception as e:
#         print("Error:", e)

#     print("\n\nExample 4")
#     try:
#         bmi = give_bmi(height4, weight4)
#         print(bmi)

#         limits = apply_limit(bmi, 25)
#         print(limits)
#     except Exception as e:
#         print("Error:", e)

#     print("\n\nExample 5")
#     try:
#         bmi = give_bmi(height5, weight5)
#         print(bmi)

#         limits = apply_limit(bmi, 25)
#         print(limits)
#     except Exception as e:
#         print("Error:", e)


# def test_42():
#     height = [1.71, 1.65, 1.73, 1.95, 1.63]
#     weight = [65.3, 58.4, 63.4, 94.5, 72.9]

#     bmi = give_bmi(height, weight)
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))

# test_42()

# my_test()
