# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''#length invariant. If this is broken we have bugs
        if (len(preorder) != len(inorder)): 
            print ('Length invariant broken')
        #Base case 
        if (len(preorder) == 0): 
            return None 
        #non-empty nodes 
        root = preorder[0]
        root_index = inorder.index(root)
        left_preorder = preorder[1:1+root_index]
        left_inorder = inorder[0:root_index]
        right_preorder = preorder[root_index+1:]
        right_inorder = inorder[root_index+1:]
        tree = TreeNode(root)
        tree.left = self.buildTree(left_preorder, left_inorder)
        tree.right = self.buildTree(right_preorder, right_inorder)
        return tree'''
        #following algorithm. Note that the first element of the preorder traversal is the root, and the location
        #of the root in the inorder traversal tells you where to split the left, right roots
        if len(preorder) != len(inorder):
            print('length invariant violated')
            return False
        if len(preorder) == 0:
            return None #base case
        root_val = preorder[0]
        #split the inorder into left, right trees
        inorder_root = inorder.index(root_val)
        inorder_left = inorder[:inorder_root]
        inorder_right = inorder[inorder_root+1:]
        preorder_left = preorder[1:len(inorder_left)+1]
        preorder_right = preorder[1+len(inorder_left):]
        root_node = TreeNode(root_val)
        root_node.left = self.buildTree(preorder_left, inorder_left)
        root_node.right = self.buildTree(preorder_right, inorder_right)
        return root_node
