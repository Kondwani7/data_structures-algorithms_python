#used to store string with the same prefix
#used in word auto completion search engines
class Trie:
    #will use hash table to store the trie
    def __init__(self, is_end=False):
        self.children = {}
        self.is_end = is_end
