#used to store string with the same prefix
#used in word auto completion search engines
class Trie:
    #will use hash table to store the trie
    def __init__(self, is_end=False):
        self.children = {}
        self.is_end = is_end
    #inserting in a trie
    def inser(self, s):
        node = self
        #for a character in a string
        for ch in s:
            if ch not in node.children:
                #insert ch
                node.children[ch] = Trie()
            #if not create it in children
            node = node.children[ch]
            #end string
        node.is_end= True
    #searching in a trie node
    def search(self, s):
        node = self
        for ch in s:
            if ch not in node.children:
                return None
            #set node to its childern and we continue
            node = node.children[ch]
        #return the node ch in the string
        return node if node.is_end else None
