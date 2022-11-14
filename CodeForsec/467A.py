n, flag = int(input()), 0

for i in range(n):
    a, b = list(map(int, input().split()))

    if a <= b - 2: flag += 1

print(flag)