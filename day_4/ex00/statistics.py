def check_input(args, kwargs):
    if len(kwargs) == 0:
        print("ERROR")
        return False

    for arg in args:
        if (type(arg) is not int):
            print("ERROR")
            return False
    
    # correct_kwargs = ["mean", "median", "quartile", "std", "var"]
    # values = kwargs.values()

    # for val in values:
    #     if correct_kwargs.__contains__(val) == False:
    #         print("ERROR")
    #         return False

    return True


def calculate_mean(nums):
    if len(nums) == 0:
        return None
    return sum(nums) / len(nums)

def calculate_median(nums):
    if len(nums) == 0:
        return None
    if len(nums) % 2 == 1:
        return nums[int(len(nums) / 2)]

    n1 = nums[int(len(nums) / 2 - 1)]
    n2 = nums[int(len(nums) / 2)]

    return (n1 + n2) / 2


def calculate_quartile(nums):
    if len(nums) == 0:
        return None
    q1 = int(1 / 4 * len(nums))
    q1 = nums[q1]

    q3 = int(3 / 4 * len(nums))
    q3 = nums[q3]

    return [q1, q3]


def calculate_var(nums):
    if len(nums) == 0:
        return None
    n = len(nums)
    mean = calculate_mean(nums)
    variance = sum((x - mean) ** 2 for x in nums) / (n)
    return variance

def custom_sqrt(number, epsilon=1e-7):
    # Initial guess for the square root
    x = number / 2.0

    while True:
        # Calculate a better approximation
        new_x = 0.5 * (x + number / x)

        # Check if the difference between the current and new approximation is within epsilon
        if abs(new_x - x) < epsilon:
            return new_x

        x = new_x

def calculate_std(nums):
    if len(nums) == 0:
        return None
    variance = calculate_var(nums)
    std = custom_sqrt(variance)
    return std



def ft_statistics(*args, **kwargs):
    if check_input(args, kwargs) is False:
        return

    nums = [num for num in args]
    props = [prop for prop in kwargs.values()]

    nums.sort()

    mean = None
    median = None
    quartile = None
    std = None
    var = None

    if props.__contains__("mean"):
        mean = calculate_mean(nums)
        if mean is not None:
            print("mean :", mean)
        else:
            print("ERROR")

    if props.__contains__("median"):
        median = calculate_median(nums)
        if median is not None:
            print("median :", median)
        else:
            print("ERROR")

    if props.__contains__("quartile"):
        quartile = calculate_quartile(nums)
        if quartile is not None:
            print("quartile :", quartile)
        else:
            print("ERROR")


    if props.__contains__("std"):
        std = calculate_std(nums)
        if std is not None:
            print("std :", std)
        else:
            print("ERROR")

    if props.__contains__("var"):
        var = calculate_var(nums)
        if var is not None:
            print("var :", var)
        else:
            print("ERROR")
    
