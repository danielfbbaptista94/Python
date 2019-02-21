c = 1


def foo():
    return c


c = 3
print(foo())


# Answer: reult is 3, because the variable C has the value of 3 when the function is called
