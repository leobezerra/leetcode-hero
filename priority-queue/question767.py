from heapq import *

class Solution:
    def reorganizeString(self, S: str) -> str:
        C = {}
        max_count = (len(S) + 1) // 2 
        for ch in S:
            count = C.get(ch, 0)  + 1
            if(count > max_count):
                return ""
            C[ch] = count

        pq = []
        for key, value in C.items():
            pq.append((-value, key))
        heapify(pq)

        result = ""
        while(len(pq) > 1):
            p1, v1 = heappop(pq)
            p2, v2 = heappop(pq)
            result += v1 + v2
            if(p1 != -1):
                heappush(pq, (p1 + 1, v1))
            if(p2 != -1):
                heappush(pq, (p2 + 1, v2))
        if(len(pq) == 1):
            result += heappop(pq)[1]
        return result 