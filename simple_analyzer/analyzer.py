class Analyzer:
	def __init__(self):
		self.numbers = []
	def add_number(self, x):
		self.numbers.append(x)
	def even_count(self):
		return sum(1 for n in self.numbers if n % 2 == 0)
	def odd_count(self):
		return sum(1 for n in self.numbers if n % 2 == 1)
	def highest_number(self):
		return max(self.numbers)
	def increasing_pairs(self):
		count = 0
		for i in range(1, len(self.numbers)):
			if self.numbers[i] > self.numbers[i-1]:
				count += 1
		return count
	def avarage(self):
		return sum(self.numbers) / len(self.numbers)
	def range_diff(self):
		return max(self.numbers) - min(self.numbers)
