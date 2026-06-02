class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter out non-alphanumeric characters and convert to lowercase
        s = [char.lower() for char in s if char.isalnum()]
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n - i - 1]:
                return False
        return True

        