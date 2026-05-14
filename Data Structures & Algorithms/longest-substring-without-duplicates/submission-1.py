class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        charSet = set()
        maxLen = 0

        for char in s:
            if char not in charSet:
                charSet.add(char)
                maxLen = max(maxLen, right - left + 1)
            else:
                while char in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(char)
            right += 1
        return maxLen