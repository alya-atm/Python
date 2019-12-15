def ankerman(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ankerman(m - 1, 1)
    elif m > 0 and n > 0:
        return ankerman(m - 1, ankerman(m, n - 1))

print(ankerman(1,3))
print(ankerman(4,2))