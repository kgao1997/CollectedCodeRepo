# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #given two non-empty linked lists representing non-negative ints
        #return the sum of the lists
        #methodology: iterate in parallel between the two lists with carry op. 
        #if one list terminates, check carry on n+1, then append the extended list to the end of the solution
        list_hd = ListNode()
        sum_lst = list_hd
        carry = False
        while (l1 != None) and (l2 != None):
            sub_sum = l1.val + l2.val
            if carry == True:
                sub_sum += 1
            if sub_sum >= 10:
                carry = True
            else:
                carry = False
            sum_lst.next = ListNode((sub_sum % 10))
            sum_lst = sum_lst.next
            l1 = l1.next
            l2 = l2.next
        #postcondition: either l1 or l2 is none
        if (l1 == None) and (l2 == None):
            if carry ==  True:
                sum_lst.next = ListNode(1)
            return list_hd.next
        elif (l1 == None):
            #l2 is not none
            while carry == True:
                if l2 != None:
                    l2.val += 1
                    if l2.val < 10:
                        carry = False
                    if l2.val == 10:
                        l2.val = 0
                    sum_lst.next = l2
                    l2 = l2.next
                    sum_lst = sum_lst.next
                else:
                    sum_lst.next = ListNode(1)
                    return list_hd.next
            sum_lst.next = l2
            return list_hd.next
        else:
            while carry == True:
                if l1 != None:
                    l1.val += 1
                    if l1.val < 10:
                        carry = False
                    if l1.val == 10:
                        l1.val = 0
                    sum_lst.next = l1
                    l1 = l1.next
                    sum_lst = sum_lst.next
                else:
                    sum_lst.next = ListNode(1)
                    return list_hd.next
            sum_lst.next = l1
            return list_hd.next
        #should never hit here
        print('Fail case')
        return False
        #pass
