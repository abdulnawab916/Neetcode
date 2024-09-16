# Note:
# You are allowed to create a Node class! 
# Any time that you want to create a linked list, you 
# HAVE to create a Node class

# things that I fixed:
# 
#
#

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
        # create counter
        counterVar = 0
        currNode = self.head
        currVal = 0 # init curr value variable
        # check the case where the index is the thing we are looking for
        if counterVar == index:
            return currNode.val # Just returning the value of the node that we are at
        # If the counterVar is not the index
        else:
            # get back the head
            currNode = self.head
            # make another counter
            secondCounter = 0
            while secondCounter < index and currNode:
                currNode = currNode.next
                currVal = currNode.val # val or value for accessing
                # forgot to iterate through the list by incrementing
                secondCounter += 1
        return currVal

    def addAtHead(self, val: int) -> None:
        # allocate space for the head by creating a new node
        newHead = Node(val)
        # newHead.next = self.head 
        # This makes sure that the next of this new head is the 'old' head
        self.head = newHead # update the head of the linked list
    
    def addAtTail(self, val: int) -> None:
        # allocate memory for a new Node
        newTailNode = Node(val) # this is how you allocate an object in Python
        # create Curr pointer to traverse
        currPointer = self.head
        # create a counter to keep track of the nodes that we are 
        # iterating through
        nodeCounter = 0
        # iterate through the list and find out what last node is
        while currPointer:
            currPointer = currPointer.next
            nodeCounter += 1
        
        # reassign head to the main head again
        currPointer = self.head
        
        # Get the actual traversal value
        actualValue = nodeCounter - 1
        
        # creating a secondCounter variablew for second iteration
        secondCounter = 0
        while secondCounter <= actualValue and currPointer:
            currPointer = currPointer.next
        
        # then, we are going to assign the currpointer next to be 
        # the new pointer that we created
        while currPointer:
            currPointer.next = newTailNode
            newTailNode.next = None # make sure tail has nothing after it

   # def addAtIndex(self, index: int, val: int) -> None:
        

    # def deleteAtIndex(self, index: int) -> None:
        


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

