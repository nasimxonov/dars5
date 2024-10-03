numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

juftmi = lambda a: a % 2 == 0

toqmi = lambda a: a % 2 != 0

juftlar = list(filter(juftmi, numbers))

toqlar = list(filter(toqmi, numbers))

print(juftlar) 
print(toqlar)   