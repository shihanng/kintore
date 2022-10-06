class Solution:
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        sum = 0

        for j in range(len(s) - 1):
            curr = self.symbols[s[j]]
            next = self.symbols[s[j + 1]]

            if curr < next:
                sum -= curr
            else:
                sum += curr

        sum += self.symbols[s[-1]]

        return sum
