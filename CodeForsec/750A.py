n, k = list(map(int, input().split()))
flag = 0

for i in range(1, n + 1):
    if k + i * 5 > 240:
        break
    k += i * 5
    flag += 1

print(flag)