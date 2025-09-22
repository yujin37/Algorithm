# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def allPossibleFBT(self, n: int) -> list[Optional[TreeNode]]:
        return self.find_All(n)
    
    def find_All(self,n):
        if n == 0:
            return []
        elif n == 1:
            return [TreeNode(0)]
        trees = []

        for left_tree_node in range(1, n, 2):
            right_tree_node = n - 1 - left_tree_node
            left_subtree = self.find_All(left_tree_node)
            right_subtree = self.find_All(right_tree_node)
            #print(left_subtree, right_subtree)
            for left_node in left_subtree:
                #print(1)
                for right_node in right_subtree:
                    root = TreeNode(0)
                    root.left = left_node
                    root.right = right_node

                    trees.append(root)
        return trees
        