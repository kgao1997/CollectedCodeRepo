# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #First implement recursively. Inorder: Visit left, node, right
        '''if root == None: 
            return [] #Base case 
        else: 
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)'''
        #Slightly tricker solution: implement iteratively using a stack 
        if root == None: 
            return []
        stack = [] 
        ret_list = []
        cur_node = root
        while (len(stack) != 0) or (cur_node != None): 
            if cur_node != None: 
                stack.insert(0, cur_node)
                cur_node = cur_node.left 
            else: 
                cur_node = stack.pop(0)
                ret_list.append(cur_node.val)
                cur_node = cur_node.right
        return ret_list
