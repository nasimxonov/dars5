list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

a = lambda l: (lambda s=set(): [s.add(tuple(i)) or i for i in l if tuple(i) not in s])()

list2 = a(list1)

print("Yangi list:", list2)
