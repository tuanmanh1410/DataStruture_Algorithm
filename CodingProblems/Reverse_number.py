###########################################################
# File name : Reverse_number.py                           #
# Description : Reverse the int number i.e : 345 to 543   #
# with Object Oriented Programming (OOP)                  #
# Author : Tuan Manh Tao                                  #
###########################################################

class Reverse():
	def __init__(self, number):
		self.nu = number

	def start(self):
		res = 0

		while(self.nu >= 1):
			res = res * 10 + self.nu % 10
			self.nu = self.nu // 10
			#print(self.nu)
		return res

a = Reverse(345)
print(a.start())

