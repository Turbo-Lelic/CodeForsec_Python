n = int(input())
arr = []
flag = 0

for i in range(n):
    arr.append(input())

for j in arr:
    if j == "X++" or j == "++X":
        flag += 1
    if j == "X--" or j == "--X":
        flag -= 1

print(flag)