class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer approach
        # first pointer at the beginning aka start of the word going forwards
        # second pointer at the end of the word going backwards
        s = [c.lower() for c in s if c.isalnum()]
        for i in range(len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True
