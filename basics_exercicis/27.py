def acceleration(v1, v2, t1, t2):
    a = (v2-v1) / (t2-t1)
    return a


v1, v2 = 0, 10
t1, t2 = 0, 20

print(acceleration(v1, v2, t1, t2))
print(acceleration(0, 10, 0, 20))
