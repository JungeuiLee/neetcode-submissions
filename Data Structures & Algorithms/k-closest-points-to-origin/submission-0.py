import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            distance = x**2 + y **2
            heapq.heappush(h, (distance, x, y))

        lst = []
        while k > 0:
            dis, x, y = heapq.heappop(h)
            lst.append([x, y])
            k -=1
        return lst