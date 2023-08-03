

def log_decorator(func):
    def wrapper(*args, **kwargs): 
        print(f"This function {func.__name__} has the following arguments: {args}\n\n")
        # printing out the result of the function with the following arguments
        result = func(*args, *kwargs)
        # multiply the result by 3 and see what you end up getting!
        print(f"This is the result of the following function being manipulated by the decorator: {result}\n\n")
        return result * 3
    print(f"This is the end of the decorator function!\n\n")
    return wrapper


@log_decorator
def euc_distance(p1, p2):
    return ((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2)

print(f"Distance multiplied by 3: {euc_distance((6, 3), (9, 1))}")
