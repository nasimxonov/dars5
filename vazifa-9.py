numbers = list(map(int, input().split()))

print(list(filter(lambda a: numbers.count(a) > 1, numbers)))