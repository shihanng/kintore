class Solution:
    def isPalindrome(self, x: int) -> bool:
        input = str(x)
        return input == input[::-1]
