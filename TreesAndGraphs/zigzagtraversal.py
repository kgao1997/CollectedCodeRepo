# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return None #base case
        is_lr = True
        zz_order_lst = []
        queue = [root]
        next_queue = []
        #print(len(queue))
        #print(((len(queue) != 0) or (len(next_queue) != 0)))
        while (len(queue) != 0) or (len(next_queue) != 0): #loop until tree is completed.
            #('in loop')
            #print(is_lr)
            #queue controls layer, next_layer is pointer to the next layer of the tree
            curr_layer_vals = []
            #print(queue)
            while(len(queue) != 0):
                curr_node = queue.pop(0)
                if is_lr == True:
                    curr_layer_vals.append(curr_node.val)
                else:
                    curr_layer_vals.insert(0, curr_node.val)
                if curr_node.left != None:
                    next_queue.append(curr_node.left)
                if curr_node.right != None:
                    next_queue.append(curr_node.right)
            #postcondition: current layer has been written
            zz_order_lst.append(curr_layer_vals)
            is_lr = not is_lr 
            queue = next_queue
            next_queue = []
        return zz_order_lst
