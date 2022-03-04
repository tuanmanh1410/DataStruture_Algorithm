'''
Implement the Atoi(string s) function, 
which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.

Check if the next character (if not already at the end of the string) is '-' or '+'. 
Read this character in if it is either. This determines if the final result is negative or positive respectively. 
Assume the result is positive if neither is present.

Read in next the characters until the next non-digit charcter or the end of the input is reached. 
The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). 
If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. 
Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
'''

class StringToInteger():
	def __init__(self, s_string):
		self.s = s_string

	def Convert(self):
		print('---------------------')
		print(self.s)
		MIN = -2**31
		MAX = 2**31 -1
		self.start = False  		# Flag for start iteger number
		self.sign = 1
		res = 0

		for i in range(0, len(self.s)):
			if (self.s[i].isdigit()):
				self.start = True
				res = res * 10 + int(self.s[i])
			elif (self.s[i] == ' ') and (self.start == False):		# Ignore space before number
				continue
			elif (self.s[i] == '+') and (self.start == False):		# Number place behind + , change flag status
				self.start = True
				self.sign = 1
			elif (self.s[i] == '-') and (self.start == False):		# Number should be place behind - , change flag status
				self.start = True
				self.sign = -1
			else: 
				break
		res = res * self.sign
		if res > MAX:
			return MAX
		if res < MIN:
			return MIN

		return res


s = StringToInteger('Test with number 42')  #Result should be return 0 due to having some word at the begining
a = s.Convert()
print('Result:', a)

s1 = StringToInteger('-43 is digit')
a1 = s1.Convert()
print('Result:', a1)




