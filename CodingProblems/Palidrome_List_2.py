###########################################################
# File name : Palidrome_List_2.py                         #
# Description : Check one linked list is Palidrome or not #
# with Object Oriented Programming (OOP)                  #
# Author : Tuan Manh Tao                                  #
###########################################################

# class Node stand for the list elements
class Node():
	def __init__(self, value):
		self.value = value
		self.next = None

# Main class of program
class Linked_List():
	def __init__(self):
		self.head = None

	def Generate(self, A):
		prev = None

		for i in A:
			curr = Node(i)
			if self.head is None:
				self.head = curr
			if prev is not None:
				prev.next = curr
			prev = curr

	def Display(self):
		temp = self.head
		while(temp):
			print(temp.value)
			temp = temp.next

	def Check_Palidrome(self):
		temp = self.head
		lenght = 0
		middle = right = left = 0

		while(temp):
			lenght +=1
			temp = temp.next
		middle = lenght // 2
		if (lenght % 2 == 0):
			right = middle + 1
			left = midđle
		else:
			left = middle - 1
			right = middle + 1

		print("Left {}, Right {}".format(left, right))


		return True

A = [1,2,4,5,4,3,1]
s = Linked_List()
s.Generate(A)
s.Display()
res = s.Check_Palidrome()


