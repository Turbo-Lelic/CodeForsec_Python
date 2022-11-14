strin = input().replace('+', '')
arr = []

for i in strin:
    arr.append(i)
arr.sort()

print('+'.join(arr))