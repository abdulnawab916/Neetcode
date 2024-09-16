# Creating a Linked List (Singly)
# Note:
# You are allowed to create a Node class! 
# Any time that you want to create a linked list, you 
# HAVE to create a Node class
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self, head, size):
        # initialize the head to be nothing
        self.head = None
        # there is nothing in the linked list yet
        self.size = 0
    
    def get(self, index: int) -> int:
        # create counter
        counterVar = 0
        currNode = self.head
        currVal = 0 # init curr value variable
        while counterVar <= index:
            currNode = currNode.next
            currValue = currNode.val
            counterVar += 1 # increment on next time we go around the loop
        return currValue

    def addAtHead(self, val: int) -> None:
        # Doesn't return anything
        # allocate space for the head by creating a new node
        newHead = new Node(val, self.head)
        # newHead.next = self.head 
        # This makes sure that the next of this new head is the 'old' head
        self.head = newHead # update the head of the linked list
    # Tip: Create  tail pointer to account for stuff. But, there could be a diff
    # Way to do this without making a tail pointer    
    def addAtTail(self, val: int) -> None:
        # allocate memory for a new Node
        newTailNode = new Node(val)
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
        while secondCounter <= actualValue:
            currPointer = currPointer.next
        
        # then, we are going to assign the currpointer next to be 
        # the new pointer that we created
        currPointer.next = newTailNode
        newTailNode.next = None # make sure tail has nothing after it

    def addAtIndex(self, index: int, val: int) -> None:
        

    def deleteAtIndex(self, index: int) -> None:
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)