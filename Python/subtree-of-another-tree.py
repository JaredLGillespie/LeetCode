# https://leetcode.com/problems/subtree-of-another-tree/


class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def compare_subtree(sroot, troot):
            if sroot is None: return troot is None
            if troot is None: return sroot is None
            if sroot.val != troot.val: return False
            return compare_subtree(sroot.left, troot.left) and \
                   compare_subtree(sroot.right, troot.right)

        def search(s, t):
            if s.val == t.val and compare_subtree(s, t): return True
            if s.left and search(s.left, t): return True
            if s.right and search(s.right, t): return True
            return False

        if not t: return not s
        return search(s, t)
