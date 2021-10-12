# Reverser list from left to right
# For example [1,2,3,4,5,6] --> [1,5,4,3,2,6]
class Linked_List(object):
	"""docstring for Liked_List"""
	def __init__(self, val = 0, next_val = None):
		self.val = val
		self.next = next_val


a = [1,2,3,4,5,6,7]

head = None
prev1 = None
curr = None

# Initialize the liked_list
for i in a:
	curr = Linked_List(i)
	if head is None:
		head = curr
	if prev1 is not None:
		prev1.next = curr
	prev1 = curr

# Start reverse linked list using prev, head, next
headnext = head.next
prev = None

while(head):
	headnext = head.next
	head.next = prev
	prev = head
	head = headnext

# End of reverse , prev become to head node
show = prev
while (show):
	print(show.val)
	show = show.next

# Show off [7,6,5,4,3,2,1] ---> This is output



