import time

# You figure out what goes in here
class LetterNode:
    def __init__(self, char):
        self.char = char
        self.is_end = ""
        self.children = {}
        self.counter = 0


class WordTree:
    def __init__(self):
        self.root = LetterNode("")

    # insert a word into the WordTree.  If you want to append any special characters,
    # do it inside this function, do not expect that the calling person will do it.
    def insert_word(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:

                new_node = LetterNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = "#"
        node.counter += 1
        

    def dfs(self,node,prefix):
        if node.is_end == "#":
            self.output.append((prefix + node.char, node.counter))
        
        for child in node.children.values():
            self.dfs(child, prefix + node.char)
            
    # check to see if a word is inside this tree
    def contains_word(self, word):
        self.output = []
        node = self.root
        
        # Check if the prefix is in the trie
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return False
        
        # Traverse the trie to get all candidates
        self.dfs(node, word[:-1])

        
        # Sort the results in reverse order and return
        mylist =  sorted(self.output, key=lambda word: word[1], reverse=True)
        for w in mylist:
            if w[0] == word:
                return True

wt = WordTree()
wt.insert_word("car")
wt.insert_word("cat")
wt.insert_word("carbon")
wt.insert_word("snack")
wt.insert_word("snake")
print(wt.contains_word("carbon"))
print(wt.contains_word("car"))
print(wt.contains_word("snack"))
print(wt.contains_word("dog"))
