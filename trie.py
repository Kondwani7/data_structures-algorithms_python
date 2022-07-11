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
    #deleting a word from a trie
    def delete(self, s):
        #start processing the deletion from the bottom of trie not top
        #to avoid deleting non target words with a similar prefix to target word
        def rec(node, s, i):
            if i == len(s):
                node.is_end = False
                return len(node.children) == 0
            else:
                #recursive deletion from bottom
                next_deletion = rec(node.children[s[i]],s, i+1)
                if next_deletion:
                    del node.children[s[i]]
                return next_deletion and not node.is_end and len(node.children) == 0
        #if word found in our trie we perform the deletion
        if self.search(s):
            rec(self, s, 0)
    #get substrings (words) of a trie
    def get_substrings(self):
        def rec(node, string, strings):
            #if we are at the end of the list
            if node.is_end:
                strings.append("".join(string))
            #only for characters in our trie
            for ch in node.children:
                string.append(ch)
                rec(node.children[ch], string, strings)
                string.pop()
        strings = []
        rec (self, [], strings)
        return strings
