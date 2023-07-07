# Do some operations on circular linked list
# Circular linked list is a linked list where all nodes are connected to form a circle. (tail.next = head)
# Generate a circular linked list, then display it

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def Generate(self, List):
        self.head = Node(List[0])
        self.tail = self.head
        for i in range (1, len(List)):
            self.tail.next = Node(List[i])
            self.tail = self.tail.next
        self.tail.next = self.head

    def Display(self):
        # Display value of each node with one line
        temp = self.head
        while (temp.next != self.head): #break loop when move to head node again
            print(temp.value, end = ' ')
            temp = temp.next
        # Display value of tail node
        print(temp.value)

A = [1,2,3,4,5,6,7,8,9,10]

Mylist = CircularLinkedList()
Mylist.Generate(A)
Mylist.Display()

