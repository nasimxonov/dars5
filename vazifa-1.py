list1 = [1, 3, 5, 7, 95, 10]

list2 = [2, 4, 6, 8]

a = lambda l1, l2: (l1.pop(), [l1.append(i) for i in l2], l1)[2]

natija = a(list1, list2)

print(natija)
