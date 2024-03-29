# Class for Singly Linked List with import data from Python list
# Refer and modify from https://www.tutorialspoint.com/
# With liked list, the head node in almost all case can be considerred as special case

# Create node for list including data and next node to link
class Node():
    def __init__(self, value): # init node with number or string
        self.value = value     # String or number depending on type of list
        self.next = None       # self.next will be Node type class
        
# Define List with head node will be initialize       
class SLinkedList():
    def __init__(self):
        self.head = None        # Type of head will be 'Node' after initializing LinkedList|From non-type to Node
        
    # Generate the linked list from integer or string list automately
    def Generate(self, a):      # Asume not empty list
        curr = None
        prev = None
        for i in a:
            curr = Node(i)
            if self.head is None:
                self.head = curr    # Assign the head node for list
            if prev is not None:
                prev.next = curr    # Create connections about the node prev.next is curr node
            prev = curr             # Store current node to previous to ready for next iteration

    # Display the value of Node
    def Display(self):
        show = self.head
        while(show): # Show the value of list from head until None
            print(show.value)
            show = show.next

    '''Insert new node at the begining of LinkedList'''
    def InsertionBegin(self, newdata):
        NewNode = Node(newdata)     # Create new node with the new data
        
        # Make newnode becoming the head node - first connect the new node to the head node
        NewNode.next = self.head # The old head node become 2nd node and keep the connection between node
        self.head = NewNode      # Assign new node to head node

        
    '''Insert new node at the end of LinkedList'''
    def InsertionEnd(self, newdata):
        NewNode = Node(newdata)     # Create new node with the new data
        if (self.head is None):     # For case empty list, 'if' condition prevents the no attribute error 
            self.head = NewNode
            return  
                                    # With empty list, 'last' will not become Node lead to no attibute 'next'
        last = self.head            # Assign node for last variable and go to the end of list
        while (last.next):          # Find the last position node until last.next == None
            last = last.next

        last.next = NewNode
    
    def Insert_Between(self, index, data): #Insert new node on the right of current node
        New = Node(data)
        temp = self.head
        for i in range(index):
            temp = temp.next	    # temp variable point the "index" position

        # Starting Insert
        New.next = temp.next        # Keep the connection between nodes inside list
        temp.next = New             # Insert the new node after assigned node

    def RemoveElement(self, keydata):
        print("Removing the " + str(keydata) + "-elements inside liked list")
        if (self.head is None):
            print('Empty List')
            return
        
        # In case head is equal to keydata
        while  (self.head.value == keydata):
            self.head = self.head.next
            if (self.head is None):
                return

        Temp = self.head
        prev = None

        while (Temp):
            if (Temp.value == keydata):     # Find down the node having value need to remove
                prev.next = Temp.next       # Remove the current node, connect previous to next node     
                Temp = Temp.next            # Ignore current temp(equal value) position and move forward 1 node, officially remove curr node
                continue                    # Go to starting point while loop

            prev = Temp                     # Store previous node, current node becomce previous node
            Temp = Temp.next                # Traverse to next node, temp has moving role


    def Reverse(self):
        head_node = self.head
        back = None
        next_node = head_node
        
        while (head_node):
            next_node = head_node.next
            head_node.next = back
            back = head_node
            head_node = next_node

        # Checking the first element
        self.head = back                # Change the self.head for the new reversed linked_list


    def CheckPalindromic(self):         # List does not change when reverse() 
        # First to get lenght of list
        iLen = 0
        temp = self.head
        while(temp):
            iLen += 1
            temp = temp.next


        # Determine the left and right position of list
        iRight = 0
        iLeft = 0
        iLeft = iLen // 2 - 1
        if ( iLen % 2 == 0):
            iRight = iLen // 2
        else:
            iRight = iLen // 2 + 1

        # Assign the left, right pointer
        p_Left = self.head
        p_right = self.head

        for i in range (0,iRight):
            if (i < iLeft):
                p_Left = p_Left.next
            p_right = p_right.next

        # Reverse the first-half of Linked List
        back = None
        next_node = self.head
        head_node = self.head
        for i in range (0, iLeft +1):
            next_node = head_node.next
            head_node.next = back 
            back = head_node
            head_node = next_node

        # Compare two-sub lists (half left reverse and half right)
        while (p_right):
            if (p_right.value != p_Left.value):
                return False
            p_right = p_right.next
            p_Left = p_Left.next

        return True

        
#Start test with list A and Initiate Liked_List

A = [1,2,3,4,3,2,1]

#Declare the list and initialize linked list from list 
MyList = SLinkedList()

MyList.Generate(A)
MyList.Display()

print(MyList.CheckPalindromic())



