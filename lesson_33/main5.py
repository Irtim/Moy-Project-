a = input().split(' ')
b = int(a[0])
c = int(a[1])
d = int(a[2])
e = 0
for i in range(1, d+1):
    e += i * b
if c - e >=0:
    print(0)
else:
    print(e - c)