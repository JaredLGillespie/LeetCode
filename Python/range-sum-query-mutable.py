# https://leetcode.com/problems/range-sum-query-mutable/


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = [0] * len(nums)
        self.BIT = [0] * (len(nums) + 1)
        for i, n in enumerate(nums): self.update(i, n)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff, self.arr[i] = val - self.arr[i], val
        i += 1
        while i < len(self.BIT):
            self.BIT[i] += diff
            i += i & -i

    def sum(self, k):
        res = 0
        while k:
            res += self.BIT[k]
            k -= k & -k
        return res

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j + 1) - self.sum(i)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
