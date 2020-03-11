import math
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def division(ar, st, fi):
	n = len(ar)
	m=math.ceil(math.sqrt(n))
	print(m)

	for i in range(m-1):
		z = ar[(i *m) : m*(i+1)]
		print (z)
	return z
division(arr, 2, 6)