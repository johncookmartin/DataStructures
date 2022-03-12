import heapq

class MyHuffman():
    def __init__(self):
        # Initialize the Huffman tree
        
        # Dictionary to hold the characters and their coressponding bitcode
        self.chars = {}
        # Huffman tree
        self.tree = None
        # Position in the bitstring being decoded
        self.decodePosition = 0

    def build(self, weights):
        # Build a huffman tree from the dictionary of character:value pairs
        
        # Build a heap of nodes from weights
        nodes = []
        for char in weights:
            node = Node(weights.get(char), char)
            heapq.heappush(nodes, node)
        
        # Create the tree from the heap of nodes
        while len(nodes) > 1:
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)
            node = Node(left.value + right.value, None, left, right)
            heapq.heappush(nodes, node)
        
        # The last node in the heap is the root of the tree
        self.tree = nodes[0]
        self.makeLookupTable(self.tree, '')
        
    
    def makeLookupTable(self, node, bitCode):
        # Recursive algorithm to fill the dictionay of characters with their coressponding bitcode
        
        if not node.data == None:
            self.chars.update({node.data:bitCode})
        else:
            self.makeLookupTable(node.left, bitCode+'1')
            self.makeLookupTable(node.right, bitCode+'0')
    
    def encode(self, word):
        # Return the bitstring of word encoded by the rules of your huffman tree
        
        bitstring = ''
        for char in word:
            bitstring += self.chars.get(char)
        return bitstring
      
    def decode(self, bitString):
        # Return the word encoded in bitstring, or None if the code is invalid
        
        word = ''
        while self.decodePosition < len(bitString):
            try:
                word += self.recursiveTraverseTree(self.tree, bitString)
            # Index or Type Error means that the code is invalid
            except:
                word = None
                break
        self.decodePosition = 0
        return word
    
    def recursiveTraverseTree(self, node, bitString):
        # Return the character after traversing the Huffman tree through the bitstring
        
        if not node.data == None:
            return node.data
        else:
            if bitString[self.decodePosition] == '1':
                self.decodePosition += 1
                return self.recursiveTraverseTree(node.left, bitString)
            elif bitString[self.decodePosition] == '0':
                self.decodePosition += 1
                return self.recursiveTraverseTree(node.right, bitString)
            else:
                return None

# This node structure might be useful to you
class Node:
    def __init__(self,value,data,left=None,right=None):
        self.value = value
        self.data = data
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.value < other.value
    
    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value
    
    def __ge__(self, other):
        return self.value >= other.value
