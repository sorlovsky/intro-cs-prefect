def listSum(a, b):
	if len(a) == 0:
		return []
	else:
		return [a[0] + b[0]] + listSum(a[1:], b[1:])


def main():
	l1 = [1, 2, 3]
	l2 = [2, 4, 5]
	print(listSum(l1, l2))

main()
