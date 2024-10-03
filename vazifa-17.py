unlilar = "aeuoi"
c = input()
n = ord(c)
m = ord(c)
right = 0
left = 0
while n < 123:
    n += 1
    if chr(n) in unlilar:
        right = n
        break

while m > 96:
    m -= 1
    if chr(m) in unlilar:
        left = m
        break

if right == 0:
    print(chr(left))
elif left == 0:
    print(chr(right))
else:
    if (right - ord(c)) > (ord(c) - left):
        print(chr(left))
    elif (right - ord(c)) < (ord(c) - left):
        print(chr(right))
    else:
        print(chr(left), chr(right))
