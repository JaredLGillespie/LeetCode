# https://leetcode.com/problems/read-n-characters-given-read4/


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        chars_read = 0
        while chars_read < n:
            buf4 = [''] * 4
            cr = read4(buf4)
            if cr == 0: break
            cr = min(cr, n - chars_read)
            buf[chars_read:] = buf4[:cr]
            chars_read += cr

        return chars_read
