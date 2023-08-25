# In python, you define a function like this
# def funcname(parameter_list):
#     pass


def sqrtRoot(param):
    return param * param


# Calling the function
print(sqrtRoot(2))

# You can also pass another function to a function as parameter


def doSomething(funcX, paramX):
    return funcX(paramX)


print(doSomething(sqrtRoot, 6))

# Lambda functions allows you to pass simple function inline without giving it a name
print(doSomething(lambda x: x * x * x, 3))