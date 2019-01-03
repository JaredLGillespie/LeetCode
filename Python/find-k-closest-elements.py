# https://leetcode.com/problems/find-k-closest-elements/


from bisect import bisect_left


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l = bisect_left(arr, x)
        if l > 0 and abs(arr[l - 1] - x) < abs(arr[l] - x): l -= 1
        r = l

        while r - l + 1 < k:
            if r + 1 >= len(arr): l -= 1
            elif l - 1 < 0: r += 1
            elif abs(x - arr[l - 1]) <= abs(arr[r + 1] - x): l -= 1
            else: r += 1

        return arr[l: r + 1]


print(Solution().findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5))
