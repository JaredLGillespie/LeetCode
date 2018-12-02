# https://leetcode.com/problems/range-sum-query-immutable/


class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.rsq = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.rsq[i] = self.rsq[i - 1] + nums[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.rsq[j + 1] - self.rsq[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
