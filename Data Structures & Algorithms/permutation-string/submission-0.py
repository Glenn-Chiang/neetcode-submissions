class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
        
        i = 0
        for j in range(len(s1), len(s2)):
            if matches == 26:
                return True

            j_char = ord(s2[j]) - ord('a')
            s2_count[j_char] += 1
            if s2_count[j_char] == s1_count[j_char]:
                matches += 1
            elif s2_count[j_char] == s1_count[j_char] + 1:
                matches -= 1
            
            i_char = ord(s2[i]) - ord('a')
            s2_count[i_char] -= 1
            if s2_count[i_char] == s1_count[i_char]:
                matches += 1
            elif s2_count[i_char] == s1_count[i_char] - 1:
                matches -= 1
            i += 1
        
        return matches == 26


             
        
            

