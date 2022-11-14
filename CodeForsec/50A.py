m, n = map(int, input().split())
x = m * n
flag = 0

for i in range(x // 2):
    x -= 2
    flag += 1

print(flag)