###########################################################
# File name : Palidrome_List_2.py                         #
# Description : Check one linked list is Palidrome or not #
# with Object Oriented Programming (OOP)                  #
# Author : Tuan Manh Tao                                  #
###########################################################

# Class Node stand for the list elements
# Base Class
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
		# STEP 1: Dẹtermine the left right position
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

		# STEP 2: Assign left and right pointer
		p_left = p_right = self.head
		for i in range(right):
			if (left > 0) and (i < left):
				p_left = p_left.next
			p_right = p_right.next

		# STEP 3: Reverse the half left of list
		head_node = self.head
		next_node = head_node
		prev_node = None
		for i in range(left+1):
			next_node = head_node.next
			head_node.next = prev_node
			prev_node = head_node
			head_node = next_node

		# STEP 4: Compare the value of each element inside two half sub_list
		while (p_right):
			if(p_left.value != p_right.value):
				return False
			p_right = p_right.next
			p_left = p_left.next

		return True

A = [1,2,4,5,4,2,1]
s = Linked_List()
s.Generate(A)
s.Display()

print(s.Check_Palidrome())


