# Class for Singly Linked List with import data from Python list
# Refer and modify from https://www.tutorialspoint.com/
# With liked list, the head node in almost all case can be considerred as special case

# Create node for list including data and next node to link
class Node():
    def __init__(self, value): # init node with number or string
        self.value = value     # String or number depending on type of list
        self.next = None       # self.next will be Node type class
        
# Define List with headval node will be initialize       
class SLinkedList():
    def __init__(self):
        self.headval = None        # Type of headval will be 'Node' after initializing LinkedList|From non-type to Node
        
    # Generate the linked list from integer or string list automately
    def Generate(self, a):         
        if (len(a)==0):
            print("Empty list, Please check again")
        else:
            self.headval = Node(a[0])  # Assign the head node with value of the first element of list
            if (len(a) >= 2):
                T = Node(a[1])         # Create the next node and assign to temp node T
                self.headval.next = T  # Keep the head node by using the temp variables connect node to linked list
            if (len(a) >= 3):
                for i in range(2, len(a), 1): # Index from 2 to len(a)-1
                    T.next = Node(a[i])    # Assign the next node with T.next attribute and keep connection
                    T = T.next

    # Display the value of Node
    def Display(self):
        show = self.headval
        while(show): # Show the value of list from head until None
            print(show.value)
            show = show.next

    '''Insert new node at the begining of LinkedList'''
    def InsertionBegin(self, newdata):
        NewNode = Node(newdata)     # Create new node with the new data
        
        #Make Newnode becoming the head node 
        NewNode.next = self.headval # The old head node become 2nd node and keep the connection between node
        self.headval = NewNode      # Assign new node to head node

        
    '''Insert new node at the end of LinkedList'''
    def InsertionEnd(self, newdata):
        NewNode = Node(newdata)    # Create new node with the new data
        if (self.headval is None): # For case empty list, 'if' condition prevents the no attribute error 
            self.headval = NewNode
            return                 # With empty list, 'last' will not become Node lead to no attibute 'next'
        last = self.headval        # Assign node for last variable and go to the end of list
        while (last.next):         # Find the last position node until last.next == None
            last = last.next

        last.next = NewNode
        
    '''Insert new node between two nodes after specific node defined before'''
    def InsertBetween(self, node, newdata):
        NewNode = Node(newdata)
        if (self.headval is None): #Check empty node or NOT
            self.headval = NewNode
            return
        if (node is None):
            print('Can not insert after this metioned node')
            return
        
        NewNode.next = node.next   # Keep the connection among nodes inside list
        node.next = NewNode        # Insert new node after specific node

    def RemoveElement(self, keydata):
        if (self.headval is None):
            print('Empty List')
            return
        
        Temp = self.headval

        if (Temp.value == keydata):
            self.headval = Temp.next        # Remove head node while Temp is head node
            Temp = None                     # Delete node temp
            return

        while (Temp is not None):
            if (Temp.value == keydata):     # Find down the node having value need to remove
                break
            prev = Temp                     # Store previous node, current node becomce previous node
            Temp = Temp.next                # Traverse to next node

        prev.next = Temp.next               # Link connection previous node to next node; ignore the current node
        Temp = None                         # Delete current node

    def Get_Lenght(self):
        temp = self.headval
        count = 1
        while (temp.next):
            temp = temp.next
            count += 1
        return count
        
#Start test with list A and Initiate Liked_List

A = [1,2,3,4,5,6]

#Declare the list and initialize linked list from list 
MyList = SLinkedList()

MyList.Generate(A)
MyList.Display()
MyList.RemoveElement(6)
MyList.Display()

