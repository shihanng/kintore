class Solution:
    def isPalindrome(self, x: int) -> bool:
        input = str(x)
        return input == input[::-1]

    def isPalindrome2(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed = 0

        while x > reversed:
            reversed = reversed * 10 + x % 10
            x = x // 10

        return x == reversed or x == reversed // 10
