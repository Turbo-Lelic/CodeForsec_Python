n = int(input())

if n <= 5:
    print(1)
else:
    if n % 5 == 0:
        print(int(n / 5))
    else:
        print(int(n / 5 + 1))