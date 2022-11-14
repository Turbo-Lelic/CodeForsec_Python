string1 = input()
flag = 0

for i in string1:
    if i == '7' or i == '4':
        flag += 1

if flag == 7 or flag == 4:
    print('YES')
else:
    print('NO')