# https://leetcode.com/problems/word-search-ii/


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

    def remove(self, word):
        def helper(word, root, index):
            if index == len(word):
                if root.end: root.end = False
                return not root.children

            elif word[index] in root.children:
                if helper(word, root.children[word[index]], index + 1):
                    root.children.pop(word[index])
                    return not root.end and not root.children

            return False

        helper(word, self.root, 0)


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def search(row, col, root):
            if root.end:
                word = ''.join(chars)
                found_words.append(word)
                word_trie.remove(word)
                if not root.children: return

            children = [k for k in root.children]

            for nr, nc in neighbors(row, col):
                for child in children:
                    if child not in root.children: continue
                    if child == board[nr][nc]:
                        board[nr][nc] = ''
                        chars.append(child)
                        search(nr, nc, root.children[child])
                        chars.pop()
                        board[nr][nc] = child

        def neighbors(row, col):
            if row > 0: yield row - 1, col
            if row < num_rows - 1: yield row + 1, col
            if col > 0: yield row, col - 1
            if col < num_cols - 1: yield row, col + 1

        if not words or not board: return []
        num_rows, num_cols = len(board), len(board[0])

        word_trie = Trie()
        for word in words:
            word_trie.add(word)

        root = word_trie.root
        chars = []
        found_words = []
        for row in range(num_rows):
            for col in range(num_cols):
                if not root.children: return found_words
                children = [k for k in root.children]

                for child in children:
                    if child not in root.children: continue
                    if child == board[row][col]:
                        board[row][col] = ''
                        chars.append(child)
                        search(row, col, root.children[child])
                        chars.pop()
                        board[row][col] = child

        return found_words
