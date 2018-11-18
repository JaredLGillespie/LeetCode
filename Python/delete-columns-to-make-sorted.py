# https://leetcode.com/problems/delete-columns-to-make-sorted/


class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        count = 0
        for i in range(len(A[0])):
            sc = 0
            for s in A:
                c = ord(s[i])
                if c >= sc: sc = c
                else:
                    count += 1
                    break

        return count
