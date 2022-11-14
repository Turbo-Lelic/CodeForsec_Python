string1 = input()
flag_b = 0
flag_m = 0

for i in string1:
    if i.isupper():
        flag_b += 1
    if i.islower():
        flag_m += 1

if flag_m == flag_b:
    print(string1.lower())

if flag_m > flag_b:
    print(string1.lower())

if flag_b > flag_m:
    print(string1.upper())