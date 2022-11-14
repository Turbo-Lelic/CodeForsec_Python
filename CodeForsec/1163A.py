n1, n2 = map(int,input().split())

def func(n1, n2):
    if n2 == 0:
        print(1)
    else:
        print(min(n1 - n2, n2))

func(n1, n2)