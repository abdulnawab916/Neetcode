# Note:
# You are allowed to create a Node class! 
# Any time that you want to create a linked list, you 
# HAVE to create a Node class

# things that I fixed:
# Had to fix the addAtHead method because I was forgetting
# to take care of the pointers and pointing it to the old head
# Took care of this!
# Got to check if the current.next exits because you cannot
# reassign to Null. This is often the convention used
# when you are working with Linked lists with loops

# What I learned about Python
# In Python, when you instantiate an object from a class, you do not
# use the 'new' keyword. All you do is that you call the
# class itself with the corresponding parameters

class Node:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next

class MyLinkedList:
    def __init__(self, head = None, size= 0):
        # initialize the head to be nothing
        self.head = None
        # there is nothing in the linked list yet
        self.size = 0
    
    def get(self, index: int) -> int:
        # Check if index is out of bounds
        if index < 0 or index >= self.size:
            return -1
        
        # Start from the head of the list
        currNode = self.head
        
        # Traverse to the node at the specified index
        for _ in range(index):
            if currNode is not None:
                currNode = currNode.next
            else:
                # If currNode is None before reaching the desired index, return -1
                return -1
        
        # Return the value at the node if currNode is not None
        return currNode.val if currNode is not None else -1
       
    
    def addAtHead(self, val: int) -> None:
        # allocate space for the head by creating a new node
        newHead = Node(val)
        # newHead.next = self.head 
        # This makes sure that the next of this new head is the 'old' head
        newHead.next = self.head # taking care of the pointers
        self.head = newHead # update the head of the linked list
        
        self.size += 1 # increment the size of our list after we add
    
    # Process of debugging
    # What I learned:
    #
    #

    def addAtTail(self, val: int) -> None:
        newTailNode = Node(val)

        # What if there is not a head?
        if not self.head:
            self.head = newTailNode
        
        # Assign the current pointer as the head
        currPointer = self.head
        # While the next node exits, then
        # we are going to find the tail
        while currPointer.next:
            currPointer = currPointer.next
        # Then we say that the tail will be the current
        # pointers node is the tail Node.
        currPointer.next = newTailNode
        
        # Then we increment the size of the linked list by '1'
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # allocate mem for new node
        newNode = Node(val)
        
        # We have to insert at (index - 1) and connect the pointer
        # to the next node

        # Steps
        # 1. Locate the position that we have to insert the node at
        currNode = self.head # finding head of the list
        counterVariable = 0
        # While the curr.next exists 
        while counterVariable < index:
            currNode = currNode.next
            counterVariable += 1
        currNode.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        currNode = self.head
        prevNode = self.head
        counterVariable = 0
        otherCounter = 0

        while otherCounter < index - 1:
            prevNode = prevNode.next
            otherCounter += 1

        while counterVariable < index and currNode.next:
            currNode = currNode.next
            counterVariable += 1

        # fixing pointers
        temp = currNode.next
        currNode.next = None
        prevNode.next = temp
                
        
    

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)

# obj.deleteAtIndex(index)

# How to work with test cases
# ["MyLinkedList","addAtHead", ]
# You have to make sure that the parameters match with the number, and then you have
# to make sure that the arrays match up and whatnot