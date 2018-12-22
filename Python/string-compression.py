# https://leetcode.com/problems/string-compression/


class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        size = 0
        prev_char = ''
        pos = 0
        num_chars = 1
        for i, c in enumerate(chars):
            if prev_char == '':
                prev_char = c
            elif prev_char == c:
                num_chars += 1
            else:
                s = str(num_chars)
                size += len(s)
                chars[pos] = prev_char
                if num_chars > 1:
                    size += 1
                    chars[pos + 1:pos + 1 + len(s)] = s

                num_chars = 1
                prev_char = c
                pos = size

        if prev_char != '':
            chars[pos] = prev_char
            s = str(num_chars)
            size += len(s)
            if num_chars > 1:
                size += 1
                chars[pos + 1: pos + 1 + len(s)] = s

        return size
