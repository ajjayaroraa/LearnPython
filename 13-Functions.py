# Defining a function

def test_func():
    # do whatever you want to do
    print("test")

test_func()


# Defining a function with parameters

def one_more(num):
    # do whatever you want to do
    print(num*3)

one_more(9)


# Defining a function with parameters and return value

def one_more_f(num):
    # do whatever you want to do
    return num*3

ret_val = one_more_f(11)
print(ret_val)
