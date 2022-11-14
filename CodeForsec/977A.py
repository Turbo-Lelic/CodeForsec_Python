n, k = map(int,input().split())

for i in range(k):
	if n % 10 != 0:
		n -= 1
	elif n % 10 == 0:
		n //= 10

print(n)