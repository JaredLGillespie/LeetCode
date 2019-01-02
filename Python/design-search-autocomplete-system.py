# https://leetcode.com/problems/design-search-autocomplete-system/


class TrieNode:
    def __init__(self):
        self.children = {}
        self.frequency = 0
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def update_sentence(self, sentence, frequency):
        root = self.root
        for c in sentence:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]

        root.frequency += frequency
        root.end = True

    def get_frequent_sentences(self, prefix, cur_node):
        def find_sentences(prefix, node):
            if node.end:
                sentences.append((-node.frequency, ''.join(prefix)))

            for c in node.children:
                prefix.append(c)
                find_sentences(prefix, node.children[c])
                prefix.pop()

        sentences = []
        find_sentences(prefix, cur_node)
        sentences.sort()

        return [s[1] for s in sentences[:3]]


class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = Trie()
        for sentence, time in zip(sentences, times):
            self.trie.update_sentence(sentence, time)

        self.cur_trie_node = self.trie.root
        self.prefix = []

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            self.trie.update_sentence(self.prefix, 1)
            self.cur_trie_node = self.trie.root
            self.prefix = []
            return []
        else:
            self.prefix.append(c)
            if self.cur_trie_node is None or c not in self.cur_trie_node.children:
                self.cur_trie_node = None
                return []
            self.cur_trie_node = self.cur_trie_node.children[c]
            return self.trie.get_frequent_sentences(self.prefix, self.cur_trie_node)

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
