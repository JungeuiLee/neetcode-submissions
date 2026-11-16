# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if root is None:
        #     return True
        
        # if root.val > self.isValidBST(root.right) and root.val < self.isValidBST(root.left):
        #     return True
        # else:
        #     return False

        def valid(node, low, high):
            if not node:    return True

            if not (low < node.val< high):
                return False
            
            L = valid(node.left, low, node.val)
            R = valid(node.right, node.val, high)
            return L and R

        return valid(root, float('-inf'), float('inf'))