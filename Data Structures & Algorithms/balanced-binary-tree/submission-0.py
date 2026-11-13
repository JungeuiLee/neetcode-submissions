# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # this functiuon return the bool whetehr height balance
        self.check = 0

        def height(node):
            # return int height differnence between left and right
            if not node:
                return 0
            L = height(node.left)
            R = height(node.right)
            
            self.check = max(self.check, abs(L-R))
            return 1 + max(L,R)
        
        height(root)
        if self.check >1:
            return False
        else:
            return True