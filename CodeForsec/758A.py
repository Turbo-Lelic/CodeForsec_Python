n, arr, flag = int(input()), list(map(int, input().split())), 0
for i in arr: flag += max(arr) - i
print(flag)