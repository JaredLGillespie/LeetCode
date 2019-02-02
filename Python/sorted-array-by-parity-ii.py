# https://leetcode.com/problems/sort-array-by-parity-ii/


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even, odd = 0, 1

        while True:
            while even < len(A) and not A[even] & 1:
                even += 2

            while odd < len(A) and A[odd] & 1:
                odd += 2

            if even >= len(A) or odd >= len(A): break
            A[odd], A[even] = A[even], A[odd]
            odd += 2
            even += 2

        return A


print(Solution().sortArrayByParityII([4,2,5,7]))
