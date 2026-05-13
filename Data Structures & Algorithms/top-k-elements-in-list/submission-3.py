class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countD = Counter(nums)
        freqCounter = [[] for _ in range(len(nums) + 1)]
        res = []

        for num, freq in countD.items():
            freqCounter[freq].append(num)
        
        for i in range(len(freqCounter)-1, -1, -1):
            for num in freqCounter[i]:
                res.append(num)
                if len(res) == k:
                    return res