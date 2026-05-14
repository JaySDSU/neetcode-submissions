class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = collections.defaultdict(int)
        maxlen = 0
        left = 0

        for right in range(len(s)):
            charCount[s[right]] += 1
            maxFreq = max(charCount.values())

            if (right - left + 1) - maxFreq > k:
                charCount[s[left]] -= 1
                left += 1
            maxlen = max(maxlen, right-left+1)
        
        return maxlen