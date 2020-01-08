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
        if (headA == None) or (headB == None): 
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
            return self.getIntersectionHelper(headA, bSubHead)
            
            
