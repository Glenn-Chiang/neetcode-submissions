class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_freq = 0
        freq = {}
        i = 0
        for j in range(len(s)):
            freq[s[j]] = freq.get(s[j], 0) + 1
            max_freq = max(max_freq, freq[s[j]])
            while j - i + 1 - max_freq > k:
                freq[s[i]] -= 1
                i += 1
            max_len = max(max_len , j - i + 1)
        return max_len