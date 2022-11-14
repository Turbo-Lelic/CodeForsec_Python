limak, bob = list(map(int, input().split()))
flag = 0

while 1:
    limak *= 3
    bob *= 2
    flag += 1

    if limak > bob:
        break

print(flag)