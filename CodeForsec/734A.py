n = int(input())
strin = input()
flag_d, flag_a = 0, 0

for i in strin:
    if i == "A": flag_a += 1
    if i == "D": flag_d += 1

if flag_d > flag_a: print("Danik")
if flag_a > flag_d: print("Anton") 
if flag_a == flag_d: print("Friendship") 