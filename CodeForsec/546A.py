x1, x2, x3 = map(int, input().split())
flag = 0

for i in range(x3 + 1):
    flag += i

if int(x1 * flag - x2) <= 0:
    print(0)
else:
    print(int(x1 * flag - x2))