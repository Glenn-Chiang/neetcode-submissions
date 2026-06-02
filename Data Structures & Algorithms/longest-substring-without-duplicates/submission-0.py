class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        i = 0
        char_set = set()

        for j in range(len(s)):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1
            length = j - i + 1
            max_len = max(max_len, length)
            char_set.add(s[j])

        return max_len