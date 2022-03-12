class MyTree():
    def __init__(self, data):
        # Initialize this node, and store data in it
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
        self.descendents = 0
        self.maxDescendents = 0
    
    def getLeft(self):
        # Return the left child of this node, or None
        return self.left
    
    def getRight(self):
        # Return the right child of this node, or None
        return self.right
    
    def getData(self):
        # Return the data contained in this node
        return self.data

    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure the tree remains complete - every level is filled save for the last, and each node is as far left as possible
        # Return this node after data has been inserted
        
        ''' Determining left or Right Insertion '''
        # Left or Right insertion is determined by using the height to 
        # know the most possible nodes at the lowest level. Then subtracting
        # total number of descendents from it determining whether the
        # resulting number is less than half of the most possible nodes. If
        # yes, the node should be inserted on the left.
        left = False
        # m is the max number of descendents from this height
        h, d, m = self.height, self.descendents, self.maxDescendents
        # f is the max number of descendents at the current working level is 2 to the power of height
        f = 2**h
        # current is how many nodes are in the current working level
        current = f - (m - d)
        # determine if current is less than half of f
        half = f//2
        if current < half:
            left = True
        # If current equals f a new level is starting so height is increased
        # Max descendents is also increased by 2**hieght
        if current == f:
            left = True
            self.height += 1
            self.maxDescendents += 2**self.height
            
        ''' Insertion '''
        # Once that is determined the number of descendents can be increased
        self.descendents += 1
        # Insert data either to the left or right of this node
        if left:
            if self.getLeft() == None:
                self.left = MyTree(data)
                return self
            else:
                self.left = self.getLeft().insert(data)
                return self
        else:
            if self.getRight() == None:
                self.right = MyTree(data)
                return self
            else:
                self.right = self.getRight().insert(data)
                return self

    def getHeight(self):
        # Return the height of this node
        return self.height  
           

class MyBST(MyTree):
    def __init__(self, data):
        # Initialize this node, and store data in it
        
        super().__init__(data)
        self.measured = 0

    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure that the tree remains a valid Binary Search Tree
        # Return this node after data has been inserted
        
        self.measured = False
        # Check if data should be sent to the left or right
        if data < self.getData():
            # Check if left is empty
            if self.left == None:
                self.left = MyBST(data)
                return self
            # Send data down the tree
            else:
                self.left = self.getLeft().insert(data)
                return self
        else:
            # Check if right is empty
            if self.right == None:
                self.right = MyBST(data)
                return self
            # Send data down the tree
            else:
                self.right = self.getRight().insert(data)
                return self
                
    def __contains__(self, data):
        # Returns true if data is in this node or a node descending from it
        
        if self.getData() == data:
            return True
        else:
            # Check the left
            if data < self.getData():
                if self.left == None:
                    return False
                else:
                    return data in self.left
            # Check the right
            else:
                if self.right == None:
                    return False
                else:
                    return data in self.right
    
    def getHeight(self):
        # Return the height of this node
        
        if not self.measured:
            left = -1 if self.getLeft() == None else self.getLeft().getHeight()
            right = -1 if self.getRight() == None else self.getRight().getHeight()
            self.height = max(left + 1, right + 1)
            self.measured = True
        return self.height  
            

class MyAVL(MyBST):
    def __init__(self, data):
        # Initialize this node, and store data in it
        
        super().__init__(data)

    def getBalanceFactor(self):
        # Return the balance factor of this node
        
        left = -1 if self.getLeft() == None else self.getLeft().getHeight()
        right = -1 if self.getRight() == None else self.getRight().getHeight()
        return left - right
                
    def insert(self, data):
        # Insert data into the tree, descending from this node
        # Ensure that the tree remains a valid AVL tree
        # Return the node in this node's position after data has been inserted
        
        # Check if data should be sent to the left or right
        if data < self.getData():
            # Check if left is empty
            if self.left == None:
                self.left = MyAVL(data)
                return self
            # Send Data down the tree
            else:
                self.left = self.getLeft().insert(data)
                # Check if node needs to rotate
                if self.getBalanceFactor() > 1:
                    # Check if there is a double rotation
                    if self.getLeft().getBalanceFactor() < 0:
                        self.left = self.getLeft().leftRotate()
                    # Rotate this node
                    return self.rightRotate()
                return self
        else:
            # Check if right is empty
            if self.right == None:
                self.right = MyAVL(data)
                return self
            # Send Data down the tree
            else:
                self.right = self.getRight().insert(data)
                #Check if node needs to rotate
                if self.getBalanceFactor() < -1:
                    #check if there is a double rotation
                    if self.getRight().getBalanceFactor() > 0:
                        self.right = self.getRight().rightRotate() 
                    # Rotate this node
                    return self.leftRotate()
                return self
                
    def leftRotate(self):
        # Perform a left rotation on this node and return the new node in its spot
                
        nodeA, nodeB, nodeC = self, self.getRight(), self.right.getLeft()
        nodeB.left, nodeA.right = nodeA, nodeC
        return nodeB
    
    def rightRotate(self):
        # Perform a right rotation on this node and return the new node in its spot
        
        nodeA, nodeB, nodeC = self, self.getLeft(), self.left.getRight()
        nodeB.right, nodeA.left = nodeA, nodeC
        return nodeB
    
    def getHeight(self):
        # Return the height of this node
        
        left = -1 if self.getLeft() == None else self.getLeft().getHeight()
        right = -1 if self.getRight() == None else self.getRight().getHeight()
        self.height = max(left + 1, right + 1)
        return self.height  
