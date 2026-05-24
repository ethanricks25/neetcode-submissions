class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = ((0-point[0]) ** 2 + (0-point[1]) ** 2) ** .5
            heap.append((dist, point))
        heapq.heapify(heap)
        k_closest = heapq.nsmallest(k, heap)
        points = [tup[1] for tup in k_closest]
        return points