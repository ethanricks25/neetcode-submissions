class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -1 * heapq.heappop(max_heap)
            y = -1 * heapq.heappop(max_heap)
            print(x, y)
            if x < y:
                y -= x
                heapq.heappush(max_heap, -1 * y)
            if y < x:
                x -= y
                heapq.heappush(max_heap, -1 * x)


        print(max_heap)
        if max_heap:
            return -1 * max_heap[0]
        return 0
