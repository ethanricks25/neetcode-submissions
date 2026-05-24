class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def intervalSort(interval):
            return interval[0]
        intervals.sort(key=intervalSort)
        res = []
        for i in range(len(intervals)):
            if len(res) == 0:
                res.append(intervals[i])
            elif res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        return res
