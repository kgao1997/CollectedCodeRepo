# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionHelper(self, headA: ListNode, headB: ListNode):
        while headA != None: 
            if (headA == headB) and (headA != None):
                return headA
            headA = headA.next 
            headB = headB.next
        #if these are ever equal to none, return out 
        return None
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #intersection point: when head.next == otherhead.next, otherhead.next = intersection point 
        #look at ways to operate in O(n) time and O(1) memory: 
        #get the length of the first and second lists. append nodes to the shorter list so the lengths are equal 
        #then iterate along both lists until an intersection is found
        '''if (headA == None) or (headB == None): 
            return None #no intersection if either is null
        lenA = 0
        aNode = headA
        while aNode != None: 
            aNode = aNode.next 
            lenA += 1 
        lenB = 0 
        bNode = headB
        while bNode != None: 
            bNode = bNode.next 
            lenB += 1 
        #go along the longer list to set the headnode to be equal to the equivalent position of the shorter list. 
        if lenA == lenB: 
            return self.getIntersectionHelper(headA, headB)
        elif lenA > lenB: #length of A is greater than the length of B 
            dif = lenA - lenB
            aSubHead = headA
            while dif > 0: 
                aSubHead = aSubHead.next 
                dif -= 1 
            return self.getIntersectionHelper(aSubHead, headB)
        else: 
            dif = lenB - lenA 
            bSubHead = headB 
            while dif > 0: 
                bSubHead = bSubHead.next 
                dif -= 1 
            return self.getIntersectionHelper(headA, bSubHead)'''
        #methodology: find the longer of the two lists, then iterate along the longer list until the length 
        #of the sublist is equivalent to the shorter list. if collision is detected along (short, sublist) pair, 
        #then return else return None
        #determine which list is longer
        if (headA == None) or (headB == None):
            return None #no list base case
        a_len = 0
        b_len = 0
        a = headA
        b = headB
        while a != None:
            a_len += 1 
            a = a.next
        while b != None:
            b_len += 1
            b = b.next
        len_indicator = 0 #0 = equal, a_longer = 1, b_longer = 2
        delta = 0
        if a_len > b_len:
            len_indicator = 1
            delta = a_len - b_len
        elif b_len > a_len:
            len_indicator = 2
            delta = b_len - a_len
        #print(delta)
        #set the pointer to point to the pseudo-head 
        if len_indicator == 1:
            pseudoA = headA
            while delta != 0:
                delta -= 1
                pseudoA = pseudoA.next
            #then check headA and headB:
            while (pseudoA != None) and (headB != None):
                #print(pseudoA.val)
                #print(headB.val)
                if (pseudoA == headB):
                    return pseudoA
                pseudoA = pseudoA.next
                headB = headB.next
            return None # if out of loop, no match
        elif len_indicator == 2:
            pseudoB = headB
            while delta != 0:
                delta -= 1
                pseudoB = pseudoB.next
            while (headA != None) and (pseudoB != None):
                if headA == pseudoB:
                    return headA
                headA = headA.next
                pseudoB = pseudoB.next
            return None
        else:
            while (headA != None) and (headB != None):
                if (headA == headB):
                    return headA
                headA = headA.next
                headB = headB.next
            return None
