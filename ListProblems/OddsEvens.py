# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None #base case
        if head.next == None:
            return head #base case
        #first node is odd, second is even, and so on
        #do this in-place
        odds_lst = ListNode()
        odds_lst.next = head
        odds_head = odds_lst #set pointer
        odds_lst = odds_lst.next
        evens_lst = ListNode()
        evens_lst.next = head.next
        evens_head = evens_lst
        evens_lst = evens_lst.next
        #use jump-stepping algorithm to resolve both lists
        while True:
            #try to apply different logic. Note that odds next = odds.next.next, evens = odds_next.next
            if (odds_lst != None) and (odds_lst.next != None):
                next_odd = odds_lst.next.next
                if next_odd != None:
                    next_even = next_odd.next
                else:
                    next_even = None
            if next_odd == None:
                odds_lst.next = evens_head.next
                return odds_head.next
            odds_lst.next = next_odd
            evens_lst.next = next_even
            odds_lst = odds_lst.next
            evens_lst = evens_lst.next
            if odds_lst.next == None:
                odds_lst.next = evens_head.next
                #test lines
                return odds_head.next
            
            '''print('odd val: ' + str(odds_lst.val))
            if evens_lst != None:
                print('even val: ' + str(evens_lst.val))
            if (odds_lst != None) and (odds_lst.next != None):
                if odds_lst.next.next == None:
                    pass
                else:
                    next_odds_lst = odds_lst.next.next
                    
            if (evens_lst != None):
                if evens_lst.next == None:
                    next_evens_lst = None
                else:
                    next_evens_lst = evens_lst.next
                #evens_lst.next = evens_lst.next.next
                
            if (odds_lst.next == None) or (next_odds_lst == None):
                print('in return statement')
                #print(head.next.val)
                #test the list for cycle
                odds_lst.next = evens_head.next #point to the even head
                while(head != None):
                    print(head.val)
                    head = head.next
                return head
            odds_lst.next = next_odds_lst
            evens_lst.next = next_evens_lst
            evens_lst = next_evens_lst
            if odds_lst != None:
                odds_lst = odds_lst.next
            if evens_lst != None:
                evens_lst = evens_lst.next'''
                
        
