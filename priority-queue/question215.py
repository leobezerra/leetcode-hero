from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pqueue = []
        for el in nums:
            heappush(pqueue, el)
            if(len(pqueue) > k):
                heappop(pqueue)
        return pqueue[0]

