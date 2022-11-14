#____________________________________________________________________0
# n1, n2 = list(map(int, input().split()))
# flag_r = min(n1, n2)
# flag_o = 0
# flag = ((n1 + n2) - (flag_r * 2)) // 2

# for i in range(flag):
#     flag_o += 1

# print(flag_r, flag_o)
#____________________________________________________________________1
# n1, n2 = list(map(int, input().split()))
# flag_r = min(n1, n2)
# flag_o = 0

# for i in range(((n1 + n2) - (flag_r * 2)) // 2):
#     flag_o += 1

# print(flag_r, flag_o)
#____________________________________________________________________2
# n1, n2 = list(map(int, input().split()))
# flag_r = min(n1, n2)
# flag_o = ((n1 + n2) - (flag_r * 2)) // 2

# print(flag_r, flag_o)
#____________________________________________________________________3
# n1, n2 = list(map(int, input().split()))
# flag_r, flag_o = min(n1, n2), ((n1 + n2) - (min(n1, n2) * 2)) // 2

# print(flag_r, flag_o)
#____________________________________________________________________4
# n1, n2 = list(map(int, input().split()))
# print(flag_r := min(n1, n2), flag_o := ((n1 + n2) - (min(n1, n2) * 2)) // 2)
#____________________________________________________________________5
n1 = list(map(int, input().split()))
print(flag_r := min(n1[0], n1[1]), flag_o := ((n1[0] + n1[1]) - (min(n1[0], n1[1]) * 2)) // 2)