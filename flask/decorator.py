def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    print ("I am in percent function")
    def inner(*args, **kwargs):
        print ("I am in inside percent function inner")
        print (func(*args, **kwargs))
        print (inner);
    return inner


@percent
def printer(msg):
    print ("I am in hello function")
    print(msg)

printer("Hello")