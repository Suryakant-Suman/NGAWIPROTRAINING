def decorator(func):
    def wrapper():
        print("Before Fuction call")
        func()
        print("After Fuction call")
    return wrapper
@decorator
def say_hello():
    print("Hello")
say_hello()

