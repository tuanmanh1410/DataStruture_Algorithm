
# Check a Linked_list is palidrome or not
# Idea: devide a list to 2 half pass from middle point and compare them
# Implement simply Singly_Liked_List

class Linked_List(object):
	"""docstring for Liked_List"""
	def __init__(self, val = 0, next_val = None):
		self.val = val
		self.next = next_val

a = [1,2,3,4,3,2,1]

head = None
prev = None
curr = None

# Initialize the liked_list
for i in a:
	curr = Linked_List(i)
	if head is None:
		head = curr
	if prev is not None:
		prev.next = curr
	prev = curr

# Get lenght of linked_list
lenght = 0
temp = head
while (temp):
	lenght += 1
	temp = temp.next

# Step 1: Determine second (half left) position  and first (half right) position 
# First and second represent for index

mid = lenght // 2
first = second = mid

if (lenght % 2) == 0:
	second -= 1
else:
	first += 1
	second -=1
print("Second:" + str(second) + " First:"+ str(first))

# Step 2: Assign second for pb (point back) | first for pf (point front)
pf = pb = head
for i in range(first):
	if (i < second) and (second != 0):
		pb = pb.next
	pf = pf.next

#Step 3, reverse a first half of list
HeadNext = head.next
prev_node = None
for i in range(second +1):
	HeadNext = head.next
	head.next = prev_node
	prev_node = head
	head = HeadNext

# Step 4, compare two half sub-list
while pf and pb:
	if (pb.val != pf.val):
		print ("False")
		exit()
	pb = pb.next
	pf = pf.next

print("True")


