# https://leetcode.com/problems/strobogrammatic-number-ii/


class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def search(index):
            if n % 2 == 0 and index == n // 2:
                numbers.append(''.join(number))
            elif n % 2 == 1 and index == n // 2:
                for i in range(len(nums_middle)):
                    number[index] = str(nums_middle[i])
                    numbers.append(''.join(number))
            else:
                for i in range(len(nums_left)):
                    if index == 0 and nums_left[i] == '0': continue
                    number[index] = str(nums_left[i])
                    number[n - index - 1] = str(nums_right[i])
                    search(index + 1)

        nums_middle = ['0', '1', '8']
        nums_left = ['0', '1', '8', '6', '9']
        nums_right = ['0', '1', '8', '9', '6']
        numbers = []
        number = ['0'] * n
        search(0)
        return numbers
