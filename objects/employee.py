


import time

class Employee(object):

	def __init__(self, birthYear, salary):
		self.birthYear = birthYear
		self.salary = salary
		self.startNewYear()

	def getBirthYear(self):
		return self.birthYear

	def getAge(self):
		return self.age

	def getSalary(self):
		return self.salary

	def getPayThisYear(self):
		return self.payThisYear

	def raiseSalary(self, increase):
		self.salary *= 1.0 + increase

	def payMonth(self):
		self.payThisYear += self.salary / 12.0

	def payBonus(self, bonus):
		self.payThisYear += bonus

	def startNewYear(self):
		self.payThisYear = 0.0
		yearsSince1970 = time.time() / (60 * 60 * 24 * 365.5)
		self.age = yearsSince1970 + (1970 - self.birthYear)

def main():
	jenny = Employee(1994, 36000)
	print(jenny)
	print(type(jenny))
	print(jenny.getBirthYear())
	print(jenny.getAge())
	jenny.payMonth()
	print(jenny.getPayThisYear())
	jenny.payBonus(11000)
	print(jenny.getPayThisYear())
	jenny.startNewYear()
	print(jenny.getPayThisYear())
	jenny.payMonth()
	print(jenny.getPayThisYear())
	jenny.raiseSalary(0.03)
	jenny.payMonth()
	print(jenny.getPayThisYear())

if __name__ == "__main__":
	main()
