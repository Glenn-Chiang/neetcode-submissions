class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_i = 0
        for i in range(len(s)):
            j = 0
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                cur_len = j * 2 + 1
                if cur_len > max_len:
                    max_len = cur_len
                    max_i = i
                j += 1  

            j = 0
            while i - j >= 0 and i + 1 + j < len(s) and s[i - j] == s[i + 1 + j]:
                cur_len = j * 2 + 2
                if cur_len > max_len:
                    max_len = cur_len
                    max_i = i
                j += 1  

        start = max_i - (max_len - 1) // 2
        return s[start: start + max_len]