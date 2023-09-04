def only_int_or_float(lst: list[int | float]) -> bool:
    for i in lst:
        if not isinstance(i, int) and not isinstance(i, float):
            return False
    return True


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
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
    if not only_int_or_float(bmi):
        raise AssertionError("bad input")

    results = []
    for i in range(len(bmi)):
        if bmi[i] > limit:
            results.append(True)
        else:
            results.append(False)
    return results
