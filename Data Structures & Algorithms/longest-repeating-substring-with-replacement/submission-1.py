class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        maxFreq = 0
        freq = {}

        i = 0
        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1
            maxFreq = max(maxFreq, freq[s[j]])
            while j - i + 1 - maxFreq > k:
                freq[s[i]] -= 1
                i += 1
            maxLength = max(maxLength, j - i + 1)
        return maxLength


        