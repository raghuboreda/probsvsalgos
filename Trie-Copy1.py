from collections import defaultdict
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = defaultdict(TrieNode)
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffix_helper(self, node, suffix='', suffixList=None):
        if len(node.children) == 0 and node.is_word:
            suffixList.append(suffix)
            return
        for child in node.children:
            self.suffix_helper(node.children[child], suffix=suffix+child, suffixList=suffixList)
        if node.is_word:
            suffixList.append(suffix)
        return

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        wordList = []
        current = self
        self.suffix_helper(current, suffix=suffix,
                           suffixList=wordList)
        return wordList
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current = self.root
        for c in word:
            current = current.children[c]
        current.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current = self.root
        for c in prefix:
            if c in current.children:
                current = current.children[c]
            else:
                return None
        return current

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod",
    "trifle", "tricity"
]
for word in wordList:
    MyTrie.insert(word)

#m = MyTrie.find("tr")
#print(m)
#print(m.suffixes())
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

f('f')


