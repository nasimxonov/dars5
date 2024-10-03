n = 8
sonlar = [1, 2, 6, 4, 3, 2, 4, 6]

natija = sorted(set(filter(lambda x: sonlar.count(x) >= 2, sonlar)))

print("Yangi sonlar:", natija)
