class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:
        if len(self.heap) == 1:
            return self.heap[0]
        if len(self.heap) == 2:
            return sum(self.heap) / 2
        if len(self.heap) % 2 == 0:
            return sum(heapq.nsmallest(len(self.heap)//2 + 1, self.heap)[-2:]) / 2
        return float(heapq.nsmallest(len(self.heap) // 2 + 1, self.heap)[-1])
        
        