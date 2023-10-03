class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end_of_word=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.is_end_of_word=True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.is_end_of_word

    def start_with(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    def start_with_print_all(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return
            cur = cur.children[c]
        self._print_all_values(cur, prefix)

    def _print_all_values(self, node, current_word):
        if node.is_end_of_word:
            print(current_word)
        for char, child in node.children.items():
            self._print_all_values(child, current_word + char)

t1=Trie()
t1.insert("apple")
t1.insert("apple_juice")
t1.insert("app")
t1.insert("banana")
print(t1.search("apple"))
print(t1.search("app"))
print(t1.start_with("app"))
t1.start_with_print_all("ap")