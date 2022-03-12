class MyTrie:
    def __init__(self):
        # Initialize the trie node as needed
        self.children = {}
        self.children_count = 0
        self.word = None
        self.autocomplete_list = []
    
    def insert(self, word):
        # Insert a word into this trie node
        
        # Check if inserting into a terminal node
        if self.isTerminal():
            # Check if there is a suffix in the node
            if self.word is not None:
                second = self.word
                self.word = None
                # Check if second was the end of a word
                if second == '':
                    self.children.update({'#':MyTrie()})
                    self.children_count += 1
                    self.autocomplete_list.append('')
                    self.insert(word)
                else:
                    self.insert(second)
                    self.insert(word)
            else:
                self.children.update({word[0]:MyTrie()})
                self.children.get(word[0]).word = word[1:]
                self.children_count += 1
                self.autocomplete_list.append(word)
        
        else:
            # Check if it is the end of the word
            if word == '':
                # Check if there is already a terminal node
                if '#' not in self.children:
                    self.children.update({'#':MyTrie()})
                    self.children_count += 1
                    self.autocomplete_list.append('')
            
            else:
                #Check if there is an available node
                if word[0] not in self.children:
                    self.children.update({word[0]:MyTrie()})
                    self.children.get(word[0]).word = word[1:]
                    self.children_count += 1
                    self.autocomplete_list.append(word)
                    
                else:
                    self.children.get(word[0]).insert(word[1:])
                    self.autocomplete_list.append(word)
            
    def exists(self, word, position=0):
        # Return true if the passed word exists in this trie node
        # A terminal node will return true if the word passed is ""
        
        # Check if word passed is in the node
        if self.word is not None:
            return self.word == word[position:]
        
        # If word passed is '', check if '#' in the node
        elif word[position:] == '':
            return '#' in self.children
        
        else:
            # If the beginning of the word is in children continue search
            if word[position] in self.children:
                return self.children.get(word[position]).exists(word, position+1)
            else:
                return False

    def isTerminal(self):
        # Return true if this node is the terminal point of a word
        
        return self.children_count == 0
        

    def autoComplete(self, prefix, position=0):
        # Return every word that extends this prefix in alphabetical order
        
        if prefix[position:] == '':
            autocomplete_result = []
            if self.word is not None:
                autocomplete_result.append(prefix + self.word)
            for i in range(len(self.autocomplete_list)):
                autocomplete_result.append(prefix+self.autocomplete_list[i])
            autocomplete_result.sort()
            return autocomplete_result
        else:
            if prefix[position] in self.children:
                return self.children[prefix[position]].autoComplete(prefix, position +1)
            else:
                return []

    def __len__(self):
        # Return the number of words that either terminate at this node or descend from this node
        # A terminal leaf should have length 1, the node A with terminal child leaves B|C should have length 2
        
        words = 0
        if self.isTerminal():
            words += 1
        for char in self.children:
            words += len(self.children.get(char))
        return words
        



