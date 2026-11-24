from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        time = 0

        for task in tasks:
            if task not in count:
                count[task] = 1
            else:
                count[task] +=1

        h = [-c for c in count.values()]
        heapq.heapify(h)

        q = deque()
        while h or q:
            time +=1

            if h:
                cnt = heapq.heappop(h) + 1
            
                if cnt != 0:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(h, q.popleft()[0])

        return time