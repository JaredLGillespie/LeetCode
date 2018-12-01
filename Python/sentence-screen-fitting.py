# https://leetcode.com/problems/sentence-screen-fitting/


class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        word_nums = [0] * len(sentence)
        word_lens = [len(word) for word in sentence]
        sentence_len = sum(word_lens) + len(sentence) - 1

        for i in range(len(sentence)):
            num_words, num_chars, word_index = 0, -1, i
            while word_index < len(sentence):
                next_num_chars = num_chars + word_lens[word_index] + 1
                if next_num_chars > cols: break
                num_words, num_chars = num_words + 1, next_num_chars
                word_index += 1

            sentences_that_fit = (cols - num_chars) // (sentence_len + 1)
            num_words += sentences_that_fit * len(sentence)
            num_chars += sentences_that_fit * (sentence_len + 1)

            word_index %= len(sentence)
            while True:
                next_num_chars = num_chars + word_lens[word_index] + 1
                if next_num_chars > cols: break
                num_words, num_chars = num_words + 1, next_num_chars
                word_index = (word_index + 1) % len(sentence)
            word_nums[i] = num_words

        num_words = 0
        for _ in range(rows):
            num_words += word_nums[num_words % len(sentence)]
        return num_words // len(sentence)
