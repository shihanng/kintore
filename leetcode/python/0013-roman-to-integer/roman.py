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
        sum, i = 0, 0

        while i < len(s):
            char = s[i]
            next = s[i + 1] if i + 1 < len(s) else None

            if char == "I" and (next == "V" or next == "X"):
                sum += self.symbols[next] - self.symbols[char]
                i += 2
            elif char == "X" and (next == "L" or next == "C"):
                sum += self.symbols[next] - self.symbols[char]
                i += 2
            elif char == "C" and (next == "D" or next == "M"):
                sum += self.symbols[next] - self.symbols[char]
                i += 2
            else:
                sum += self.symbols[char]
                i += 1

        return sum
