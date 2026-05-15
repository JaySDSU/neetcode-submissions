class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for ind, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                resT, resI = stack.pop()
                res[resI] = ind - resI
            stack.append([temp,ind])
        
        return res