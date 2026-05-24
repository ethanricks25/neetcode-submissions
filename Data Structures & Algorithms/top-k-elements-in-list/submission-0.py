class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        arr = []

        for num in nums:
            if num not in d:
                d[num] = 0
            else:
                d[num] += 1
        for _ in range(k):
            max_key = max(d, key=d.get)
            arr.append(max_key)
            d.pop(max_key)
        
        return arr
