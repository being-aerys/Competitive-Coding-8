# Created by Aashish Adhikari at 12:47 PM 2/15/2021

'''
Time Complexity:
O(n) where n is the number of nodes in the tree.

Space Complexity:
O(n) as we create temporary variables at each node.

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def recurse(self, node):


        # base case

        if node.left is None and node.right is None:

            return node

        if node.left is None:
            return self.recurse(node.right)

        if node.right is None:
            node.right = node.left
            node.left = None
            return self.recurse(node.right)


        # logic

        temp_left = node.left
        temp_right = node.right

        node.right = temp_left
        returned = self.recurse(node.right)


        node.left = None

        returned.right = temp_right

        if returned.right is not None:
            return self.recurse(returned.right)




    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is not None:
            self.recurse(root)
