# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, tree, height) -> int:
        if not tree:
            return height
        else:
            left = self.helper(tree.left, height+1)
            right = self.helper(tree.right, height+1)
            if abs(left - right) > 1:
                return -1
            else:
                return max(left, right)
        
        
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        left_nood = root.left
        right_nood = root.right
        left_h = self.helper(left_nood, 1)
        right_h = self.helper(right_nood, 1)
        
        if left_h < 0 or right_h < 0:
            return False
        if abs(left_h - right_h) > 1:
            return False
        return True