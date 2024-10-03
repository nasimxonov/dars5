def kopaytma(n):

    result = 1

    for i in range(1, n + 1):

        result *= i

    return result

result = kopaytma(5)

print(result)
