# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)  # join() returns an iterable
        kwargs_value = ", ".join(f"{k}:{v}" for k, v in kwargs.items())
        print(
            f"calling: {func.__name__}()\nwith args {args_value} and kwargs {kwargs_value}"
        )
        result = func(*args, **kwargs)
        return result

    return wrapper


@debug
def greet(name, greeting="hello"):
    print(f"{greeting}, {name}")


greet("chai", greeting="hanji")
