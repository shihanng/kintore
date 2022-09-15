class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = 0

        while n <= len(s):
            i = n + 1
            while i <= len(s):
                p = s[n:i]

                if p == p[::-1]:
                    res = p if len(res) < len(p) else res

                i += 1

            n = n + 1

        return res
