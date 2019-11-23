from heapq import * 

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if(head == None):
            return head
        pqueue = []
        current = head
        i = 0
        while(current != None):
            val = current.val
            heappush(pqueue, (0 if val < x else 1, i, val))
            current = current.next
            i += 1
        newhead = ListNode(heappop(pqueue)[2])
        current = newhead
        while(len(pqueue) > 0):
            current.next = ListNode(heappop(pqueue)[2])
            current = current.next
        return newhead