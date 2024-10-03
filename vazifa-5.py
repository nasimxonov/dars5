list1 = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'wcdsw', 'sdfsd', 'dagfa', 'acjd']

a = list(filter(lambda a: a[0] == 'a', list1))

d = list(filter(lambda a: a[0] == 'd', list1))

w = list(filter(lambda a: a[0] == 'w', list1))

print("a:",a)
print("d:",d)
print("w:",w)