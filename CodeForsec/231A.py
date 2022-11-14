n = int(input())
f = 0

for i in range(n):
    x, x1, x2 = list(map(int, input().split()))

    if x + x1 + x2 >= 2:
        f += 1

print(f)