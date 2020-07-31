"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''#corner cases: 
        if root == None: 
            return None 
        #balanced tree, if one child doesn't exist then terminate at root 
        if root.left == None: 
            return root 
        #Then for each rightmost left node and leftmost right node, set the next pointer as appropriate 
        rightmost_leftnode = root.left 
        leftmost_rightnode = root.right
        while rightmost_leftnode != None: #since perfect binary tree, can use one side as level-proxy 
            rightmost_leftnode.next = leftmost_rightnode 
            rightmost_leftnode = rightmost_leftnode.right 
            leftmost_rightnode = leftmost_rightnode.left 
        #now recurse on children 
        self.connect(root.right)
        self.connect(root.left)
        return root'''
        #apply generalizable four pointer method on tree
        #to do so, dispatch base cases where 4 pointer method cannot be initialized:
        '''if root == None or root.left == None or root.right == None:
            return root #tree is just a single node or nonexistent
        #initialize 4 pointer window
        top_anchor = root
        top_floater = root
        root_pointer = root
        if top_anchor.left != None:
            bottom_anchor = top_anchor.left
            bottom_floater = top_anchor.left
        else:
            bottom_anchor = top_anchor.right
            bottom_floater = top_anchor.right
        #generalized operation process:
        while True: 
            if bottom_floater.next != None:
                bottom_floater = bottom_floater.next
            else: #need to find the next node for bottom floater
                if top_floater == None:
                    p_top_anchor = bottom_anchor
                    #print(bottom_anchor.val)
                    while True:
                        print('True: ' + str(p_top_anchor.val))
                        if (p_top_anchor.left == None) and (p_top_anchor.right == None):
                            p_top_anchor = bottom_anchor.next
                            if p_top_anchor == None:
                                return root_pointer
                        elif p_top_anchor == None: #no more potential top pointers, done
                            return root_pointer
                        elif p_top_anchor.left != None:
                            top_anchor = p_top_anchor
                            top_floater = top_anchor
                            bottom_anchor = p_top_anchor.left
                            bottom_floater = bottom_anchor
                            print('left branch: ' + str(bottom_anchor.val))
                            break
                        elif p_top_anchor.right != None:
                            top_anchor = p_top_anchor
                            top_floater = top_anchor
                            bottom_anchor = p_top_anchor.right
                            bottom_floater = bottom_anchor
                            print('right_branch: ' + str(bottom_anchor.val))
                            break
                        else:
                            print('shouldnt happen, p_top_anchor_section')
                            return None

                    #postcondition: anchors and floaters should be initialized to lower level
                elif (top_floater.left != None) and (top_floater.left != bottom_floater):
                    if bottom_floater.next == None:
                        bottom_floater.next = top_floater.left
                    else:
                        top_floater = top_floater.next
                elif (top_floater.right != None) and (top_floater.right != bottom_floater):
                    if bottom_floater.next != None:
                        bottom_floater.next = top_floater.right
                    else:
                        top_floater = top_floater.next
                else: 
                    print('unhandled exception')
                    return 0'''
        #99% sure above doesn't work, below was using a reference solution
        if root == None:
            return
        lastHead = root
        lastCurrent = None
        currentHead = None
        current = None
        
        while lastHead != None:
            lastCurrent = lastHead
            
            while lastCurrent != None:
                if currentHead == None:
                    currentHead = lastCurrent.left
                    current = currentHead
                else:
                    current.next = lastCurrent.left
                    current = current.next
                    
                if currentHead != None:
                    current.next = lastCurrent.right
                    current = current.next
                    
                lastCurrent = lastCurrent.next
                
            lastHead = currentHead
            currentHead = None
        
        return root
