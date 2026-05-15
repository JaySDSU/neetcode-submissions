class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Count, s2Count = [0]*26, [0]*26
        matches = 0
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        left = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            curr_ind = ord(s2[i]) - ord('a')
            s2Count[curr_ind] += 1
            if s2Count[curr_ind] == s1Count[curr_ind]:
                matches += 1
            elif s2Count[curr_ind] == s1Count[curr_ind] + 1:
                matches -= 1
            
            curr_ind = ord(s2[left]) - ord('a')
            s2Count[curr_ind] -= 1
            if s2Count[curr_ind] == s1Count[curr_ind]:
                matches += 1
            elif s2Count[curr_ind] == s1Count[curr_ind] - 1:
                matches -= 1
            left += 1
        return matches == 26