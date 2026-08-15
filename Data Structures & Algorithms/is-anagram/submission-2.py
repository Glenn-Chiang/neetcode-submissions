class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        for ch in t:
            count[ch] = count.get(ch, 0) - 1

        for ch in count:
            if count[ch] != 0:
                return False
        
        return True