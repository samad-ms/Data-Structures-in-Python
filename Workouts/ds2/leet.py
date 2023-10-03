class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

# Example usage
trie = Trie()

# Inserting words into the trie
trie.insert("apple")
trie.insert("banana")
trie.insert("cat")
trie.insert("dog")

# Searching for words in the trie
print(trie.search("cat"))  # True
print(trie.search("apple"))  # True
print(trie.search("banana"))  # True
print(trie.search("dog"))  # True
print(trie.search("elephant"))  # False

# Checking if a prefix exists in the trie
print(trie.starts_with("ca"))  # True
print(trie.starts_with("do"))  # True
print(trie.starts_with("ap"))  # True
print(trie.starts_with("b"))  # True
print(trie.starts_with("ele")) # False
print(trie.root.children)