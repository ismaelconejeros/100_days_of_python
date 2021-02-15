# Advanced Decorators
# Instructions
# Create a logging_decorator() which is going to log the name of the function that was called, the arguments it was given and finally the returned output.

# HINT 1: You can use function.__name__ to get the name of the function.
# HINT 2: You'll need to use *args

# Create the logging_decorator() function 👇

def logging_decorator(function):
    def log(*args, **kwargs):
        print(f"You called the {function.__name__}{args} function")
        print(f"it returned {function(*args)}")
    return log

# Use the decorator 👇

@logging_decorator
def sum_function(a,b):
    return a + b

sum_function(2,3)