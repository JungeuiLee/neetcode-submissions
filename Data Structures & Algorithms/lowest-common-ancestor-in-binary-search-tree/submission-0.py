# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # case1 - p and q are both child(root.left | root.right.right)
        # case2 - p or q is parent and other q or p is child

        if p.val < root.val  and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val  and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

        # if (root.left == p and root.right==q)or (root.left == q and root.right==p):
        #     return root.val
    
    # def subTree(self, root:TreeNode, subTree:TreeNode) -> bool:
    #     if not root:
    #         return False
    #     if 
        
    #     if self.subTree(root.left, subTree) or self.subTree(root.right, subTree):
    #         return 