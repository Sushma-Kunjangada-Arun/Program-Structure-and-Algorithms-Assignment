############################################################
# Write code in file solution.py 
# Post� solution.py in Canvas along with 4 screen shots that shows Leetcode has passed. We will not use screen shot to give 100
# Cut and paste the whole solution.py file in Leetcode and run. All tests must pass
# Note that you should do 4 times in 225, 232,622 and 641
# TA will run solution.py file 4 times in 225, 232,622 and 641
# All tests must pass for 100
########################################################### 

class ListNode:
    #NOTHING CAN BE CHANGED HERE
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next
         
            
############################################################
#  class  Slist
###########################################################   
class Slist():
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0 
        
    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################

    ########################################################### 
    # Prepend: add a node at the begining of slist
    # Time: THETA(1)
    # Space: THETA(1)
    ########################################################### 
    def prepend(self, a: 'int'):
        self._len = self._len + 1
        self._build_node(a, False)

    ########################################################### 
    # Build a node and add it to the beginning/end
    # Time: THETA(1)
    # Space: THETA(1)
    ########################################################### 
    def _build_node(self, i: 'int', append:'bool' = True):
        n = ListNode(i)
        #empty
        if(self._first == None and self._last == None):
            self._first = n
            self._last = n
        else:
            if(append):
                self._last.next = n
                self._last = n
            else:
                n.next = self._first
                self._first = n

    ########################################################### 
    # Get number of elements in the slist
    # Time: THETA(n)
    # Space: THETA(1)
    ########################################################### 
    def __len__(self)->'int':
        return self._len

    ########################################################### 
    # Get the first element in slist
    # Time: THETA(1)
    # Space: THETA(1)
    ########################################################### 
    def get_front_element(self)->'T':
        if(self._first):
            return self._first.val
        else:
            return -1

    ########################################################### 
    # Delete the first element in slist
    # Time: THETA(1)
    # Space: THETA(1)
    ########################################################### 
    def delete_front_element(self)->'bool':
        if(self._first):
            nodes = [self._first, None]
            a = self._remove(nodes)
            return a;
        else:
            return False

    ########################################################### 
    # Delete an element in slist
    # Time: O(n)
    # Space: THETA(1)
    ########################################################### 
    def _remove(self, nodes: 'slist of size 2')->'bool':
        if(nodes[0]):
            currentNode = nodes[0]
            previousNode = nodes[1]
            if((currentNode == self._first) and (currentNode == self._last) and (previousNode == None)):
                #Only 1 element
                assert(self._first == self._last)
                self._first = None
                self._last = None
            elif(currentNode == self._first):
                #list has more than 1 element and first element is being removed
                assert(self._first.next != None)
                self._first = currentNode .next
            elif(currentNode == self._last):
                #list has more than 1 element and last element is being removed
                assert(self._first)
                previousNode.next = None
            self._len -= 1
            return True

    ########################################################### 
    # Append: add a node at the end of slist
    # Time: THETA(1)
    # Space: THETA(1)
    ########################################################### 
    def append(self, a: 'int'):
        self._len = self._len + 1
        self._build_node(a, True)

    ########################################################### 
    # Get the last element in slist
    # Time: THETA(1)
    # Space: THETA(1)
    ########################################################### 
    def get_last_element(self)->'T':
        if(self._first):
            assert(self._last)
            return self._last.val
        else:
            return -1

    ########################################################### 
    # Delete the last element in slist
    # Time: THETA(n)
    # Space: THETA(1)
    ########################################################### 
    def delete_last_element(self) -> bool:
        if (self._first == None):
            return False

        # If there is only one element
        if (self._first == self._last):
            self._first = None
            self._last = None
        else:
            # Traverse to the second-to-last node
            current = self._first
            prev = None
            while current.next is not None:
                prev = current
                current = current.next
            
            # Update the last node
            prev.next = None
            self._last = prev

        self._len -= 1
        return True



  
############################################################
#  class  MyStack
#225. Implement Stack using Queues

#https://leetcode.com/problems/implement-stack-using-queues
########################################################### 
class MyStack:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    def push(self, a: int) -> None:
        self._s.prepend(a)

    def pop(self) -> int:
        a = self._s.get_front_element()
        self._s.delete_front_element()
        return a

    def top(self) -> int:
        return(self._s.get_front_element())

    def empty(self) -> bool:
        length = len(self._s)
        if( length == 0):
            return True
        return False

############################################################
#  class  MyQueue
#232. Implement Queue using Stacks

# https://leetcode.com/problems/implement-queue-using-stacks/
########################################################### 
class MyQueue:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    def push(self, a: int) -> None:
        self._s.append(a)

    def pop(self) -> int:
        a = self._s.get_front_element()
        self._s.delete_front_element()
        return a

    def peek(self) -> int:
        return(self._s.get_front_element())

    def empty(self) -> bool:
        length = len(self._s)
        if( length == 0):
            return True
        return False


############################################################
#  MyCircularQueue
# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/
########################################################### 

class MyCircularQueue:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()

    def enQueue(self, value: int) -> bool:
        if(self.isFull()):
            return False
        self._s.append(value)
        return True

    def deQueue(self) -> bool:
        if(self.isEmpty()):
            return False
        self._s.delete_front_element()
        return True

    def Front(self) -> int:
        return(self._s.get_front_element())

    def Rear(self) -> int:
        return(self._s.get_last_element())

    def isEmpty(self) -> bool:
        length = len(self._s)
        if( length == 0):
            return True
        return False

    def isFull(self) -> bool:
        length = len(self._s)
        if( self._K == length):
            return True
        return False
 

############################################################
#  MyCircularDeque
#641. Design Circular Deque
#https://leetcode.com/problems/design-circular-deque

###########################################################  
class MyCircularDeque:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()

    def insertFront(self, value: int) -> bool:
        if(self.isFull()):
            return False
        self._s.prepend(value)
        return True

    def insertLast(self, value: int) -> bool:
        if(self.isFull()):
            return False
        self._s.append(value)
        return True

    def deleteFront(self) -> bool:
        if(self.isEmpty()):
            return False
        self._s.delete_front_element()
        return True

    def deleteLast(self) -> bool:
        if(self.isEmpty()):
            return False
        self._s.delete_last_element()
        return True

    def getFront(self) -> int:
        return(self._s.get_front_element())

    def getRear(self) -> int:
        return(self._s.get_last_element())

    def isEmpty(self) -> bool:
        length = len(self._s)
        if( length == 0):
            return True
        return False

    def isFull(self) -> bool:
        length = len(self._s)
        if( self._K == length):
            return True
        return False
 
