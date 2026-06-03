class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLength = 0
        maxCenter = 0

        for i in range(n):
            j = 0
            # Odd length palindrome
            while i - j >= 0 and i + j < n and s[i- j] == s[i + j]:
                length = 2 * j + 1
                if length > maxLength:
                    maxLength = length
                    maxCenter = i
                j += 1
            j = 0
            # Even length palindrome
            while i - j >= 0 and i + j + 1 < n and s[i - j] == s[i + j + 1]:
                length = 2 * j + 2
                if length > maxLength:
                    maxLength = length
                    maxCenter = i
                j += 1
        
        start = maxCenter - (maxLength - 1) // 2
        return s[start : start + maxLength]
