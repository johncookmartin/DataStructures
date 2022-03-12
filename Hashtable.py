class MyHashTable():
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the function hash1
        
        self.hashtable = [None] * size
        self.hash1 = hash1
        self.length = 0
    
    def put(self, key, data):
        # Store data with the key given, return true if successful or false if the data cannot be entered
        # On a collision, the table should not be changed
        
        myhash = self.hash1(key)
        if self.hashtable[myhash] is None:
            self.hashtable[myhash] = Node(key, data)
            self.length += 1
            return True
        else:
            return False
    
    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist
        
        myhash, data = self.hash1(key), None
        if self.hashtable[myhash] is not None:
            if self.hashtable[myhash].key == key:
                data = self.hashtable[myhash].data
        return data
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        
        return self.length

    def isFull(self):
        # Returns true if the HashTable cannot accept new members
        
        return self.length == len(self.hashtable)
        

class MyChainTable(MyHashTable):
    def __init__(self, size, hash1):
        # Create an empty hashtable with the size given, and stores the function hash1
        super().__init__(size,hash1)
    
    def put(self, key, data):
        # Store the data with the key given in a list in the table, return true if successful or false if the data cannot be entered
        # On a collision, the data should be added to the list
        
        insertnode = self.hashtable[self.hash1(key)]
        if insertnode is None:
            self.length += 1
            self.hashtable[self.hash1(key)] = Node(key, data)
            return True
        else:
            while insertnode.chain is not None:
                insertnode = insertnode.chain
            self.length += 1
            insertnode.chain = Node(key, data)
            return True

    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist 
        
        currentnode = self.hashtable[self.hash1(key)]
        while currentnode is not None:
            if currentnode.key == key:
                return currentnode.data
            else:
                currentnode = currentnode.chain
        return None
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        
        return self.length

    def isFull(self):
        # Returns true if the HashTable cannot accept new members
        
        return False

class MyDoubleHashTable(MyHashTable):
    def __init__(self, size, hash1, hash2):
        # Create an empty hashtable with the size given, and stores the functions hash1 and hash2
        
        super().__init__(size,hash1)
        self.hash2 = hash2
    
    def put(self, key, data):
        # Store data with the key given, return true if successful or false if the data cannot be entered
        # On a collision, the key should be rehashed using some combination of the first and second hash functions
        # Be careful that your code does not enter an infinite loop
        
        first = self.hash1(key)
        if self.hashtable[first] is None:
            self.hashtable[first] = Node(key, data)
            self.length += 1
            return True
        else:
            second = self.hash2(first)
            step = first - second
            if step < 0:
                step += len(self.hashtable)
            while self.hashtable[step] is not None:
                step -= second
                if step < 0:
                    step += len(self.hashtable)
                if step == first:
                    return False
            self.hashtable[step] = Node(key, data)
            self.length += 1
            return True                    
    
    def get(self, key):
        # Returns the item linked to the key given, or None if element does not exist
        
        first = self.hash1(key)
        if self.hashtable[first] is not None:
            if self.hashtable[first].key == key:
                return self.hashtable[first].data
            else:
                second = self.hash2(first)
                step = first - second
                if step < 0:
                    step += len(self.hashteable)
                while self.hashtable[step].key != key:
                    step -= second
                    if step < 0:
                        step += len(self.hashtable)
                    if step == first:
                        return None
                return self.hashtable[step].data
        
    def __len__(self):
        # Returns the number of items in the Hash Table
        
        return self.length



class Node:
    def __init__(self, key, data, node=None):
        # Initialize this node, insert data, and set the next node if any
        self.key=key
        self.data=data
        self.chain=node
