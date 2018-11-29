# https://leetcode.com/problems/word-squares/


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        root = self.root
        for c in word:
            if c not in root.children: root.children[c] = TrieNode()
            root = root.children[c]
        root.end = True


class Solution(object):
    def build_word_trie(self, words):
        trie = Trie()
        for word in words: trie.add(word)
        return trie

    def validate_word(self, col, word_trie, word, square):
        for row in range(col, len(square)):
            node = word_trie.root
            for i in range(0, col):
                if square[row][i] not in node.children: return False
                node = node.children[square[row][i]]
            if word[row] not in node.children: return False
        return True

    def find_potential_words(self, col, word_trie, square):
        def search_potential_words(node):
            if node.end:
                potential_words.append(word[:])
            else:
                for c in node.children:
                    word.append(c)
                    search_potential_words(node.children[c])
                    word.pop()

        word = []
        node = word_trie.root
        for i in range(0, col):
            if square[col][i] not in node.children: break
            word.append(square[col][i])
            node = node.children[square[col][i]]
        else:
            potential_words = []
            search_potential_words(node)
            return [word for word in potential_words if self.validate_word(col, word_trie, word, square)]
        return []

    def place_word(self, col, word, word_length, square):
        for i in range(col, word_length):
            square[col][i] = word[i]
            square[i][col] = word[i]

    def wordSquaresHelper(self, col, word_trie, word_length, squares, square):
        if col == word_length:
            squares.append([''.join(s) for s in square])
            return

        for word in self.find_potential_words(col, word_trie, square):
            self.place_word(col, word, word_length, square)
            self.wordSquaresHelper(col + 1, word_trie, word_length, squares, square)

    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        squares = []
        word_length = len(words[0])
        square = [[''] * word_length for _ in range(word_length)]
        word_trie = self.build_word_trie(words)
        self.wordSquaresHelper(0, word_trie, word_length, squares, square)
        return squares
