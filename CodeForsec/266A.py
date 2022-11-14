n = int(input())
rgb = input()
flag = 0

for i in range(len(rgb) - 1):
    if rgb[i] != rgb[i + 1]:
        pass
    else:
        flag += 1

print(flag)