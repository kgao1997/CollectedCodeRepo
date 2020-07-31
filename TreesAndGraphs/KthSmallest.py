# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        def operatorHelper(node, k):
            if node.left == None: 
                if k - 1 == 0:
                    return node, 0 #node found
                elif node.right == None:
                    return node, k - 1 #left and right subtrees are null
                else:
                    return operatorHelper(node.right, k-1)
            else:
                left_node, k_remaining = operatorHelper(node.left, k)
                if k_remaining == 0: #node found
                    return left_node, k_remaining 
                else:
                    if k_remaining - 1 == 0:
                        return node, 0 #check self before going right
                    
                    if node.right != None:
                        right_node, k_remaining = operatorHelper(node.right, k_remaining - 1) #explore right
                        if k_remaining == 0: #node found
                            return right_node, k_remaining
                        else:
                            return node, k_remaining
                    else:
                        return node, k_remaining - 1
                    
        node, k_remaining = operatorHelper(root, k)
        return node.val
