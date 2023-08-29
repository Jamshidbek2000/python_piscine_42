def ft_filter(ft, items) -> object:
    if ft:
        return [item for item in items if ft(item)]
    return [item for item in items if item]
    # filtered_items = []
    # for item in items:
    #     if ft(item) == True:
    #         filtered_items.append(item)
    # return filtered_items


def is_odd(number) -> bool:
    return number % 2 == 1


def is_even(number) -> bool:
    return number % 2 == 0


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    print(ft_filter(is_odd, numbers))
    print(ft_filter(is_even, numbers))


if __name__ == "__main__":
    main()
