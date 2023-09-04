def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwds):
            try:
                nonlocal count
                if count < limit:
                    count += 1
                    return function(*args, **kwds)
                else:
                    raise ValueError(f"{function} call too many times")
            except Exception as e:
                  print("Error:", e)
        return limit_function

    return callLimiter
