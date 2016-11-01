


import math
import turtle



# Computes Paul's monologue length.
# Input: Positive integer n.
# Returns: Positive integer.
def monologueLength(n):
	if n == 1:
		return 1
	elif n % 2 == 0:
		return 1 + monologueLength(n // 2)
	else:
		return 1 + monologueLength(3 * n + 1)

# Computes the combination function n! / (k! (n - k)!).
# Input: Nonnegative integer n. Integer k such that 0 <= k <= n.
# Returns: Positive integer.
def choose(n, k):
	if k == 0 or k == n:
		return 1
	else:
		return choose(n - 1, k) + choose(n - 1, k - 1)

# Draws a dragon fractal.
# Inputs: turtle. Float. Nonnegative integer.
# Returns: None.
def drawDragon(t, length, detail):
	if detail == 0:
		t.forward(length)
	else:
		t.right(45)
		drawDragon(t, length / 4.0 * math.sqrt(2.0), detail - 1)
		t.left(90)
		drawDragon(t, length / 2.0 * math.sqrt(2.0), detail - 1)
		t.right(90)
		drawDragon(t, length / 4.0 * math.sqrt(2.0), detail - 1)
		t.left(45)

# Computes the sum of two lists of numbers (of equal length >= 0).
# If the lists are empty, then returns the empty list.
# Input: List of numbers. List of numbers of the same length.
# Returns: List of numbers of the same length.
def listSum(a, b):
	if len(a) == 0:
		return []
	else:
		return [a[0] + b[0]] + listSum(a[1:], b[1:])

# Computes the sum of two arrays of numbers.
# Input: Array of numbers. Array of numbers of the same dimensions.
# Returns: Array of numbers of the same dimensions.
def arraySum(a, b):
	if type(a) == float or type(a) == int:
		print(a, b)
		return a + b

	else:
		# We could replace the looping with another recursion, but let's not.
		new = []
		for i in range(len(a)):
			print("hello")
			new += [arraySum(a[i], b[i])]
		print(new)
		return new

def main():
	# print(monologueLength(5))
	# print(choose(4, 2))
	# drawDragon(turtle.getturtle(), 200, 5)
	# print(listSum([1, 2, 3], [4, 5, 6]))
	# first = [[[[0, 1, 1], [1, -1, 4]], [[2, 1, 2], [3, 3, 1]], [[-5, -1, 3], [2, 2, 2]]]]
	# second = [[[[5, 2, 2], [1, -1, 7]], [[2, 0, 0], [3, 9, 4]], [[4, 4, 4], [2, 2, 2]]]]


	# first = [[1, 2, 3], [1, 2, 3]]
	# second = [[2, 4, 1], [1, 2, 3]]
	first = [1, 2]
	second = [2, 3]
	print(arraySum(first, second))

if __name__ == "__main__":
	main()
