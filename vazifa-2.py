list1 = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9 , 7, 1]

nol = lambda l1: ([i for i in l1 if i != 0] + [0] * l1.count(0))

natija = nol(list1)

print("Yangi list:", natija)
