n = int(input())
arr = []
glob = []

for i in range(n):
    arr.append(input())

for j in arr:
    if len(j) > 10:
        glob.append(j[0] + str(len(j) - 2) + j[-1])
    else:
        glob.append(j)

for l in glob:
    print(l)