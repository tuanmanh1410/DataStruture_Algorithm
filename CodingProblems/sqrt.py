# Find Sqrt() without math function 
# Reduce the range between upper and lower with defined limit for test

class My_Number():
	def __init__(self, number):
		self.num = number

	def Sqrt(self):
		limit = 0.0001
		upper = self.num
		lower = 0
		res = 1

		while (abs(res*res - self.num) > limit):
			res = (upper + lower)/2
			# Reduce the gap of upper and lower bound; get the average to get the sqrt(x)
			if (res*res >= self.num):
				upper = res
			else:
				lower = res
		return res

a = My_Number(4)
print(a.Sqrt())
