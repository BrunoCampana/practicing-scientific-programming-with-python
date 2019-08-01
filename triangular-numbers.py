def triangular_numbers(n):
    i, t = 1, 0

    while i <= n:
        yield t
        t += i
        i += 1

print(list(triangular_numbers(15)))
