def foo():
    c = 1
    return c


# def foo2():
#     global c
#     c = 1
#     return c


foo()
# foo2()
print(c)

# Answer: error because c is a local variable
