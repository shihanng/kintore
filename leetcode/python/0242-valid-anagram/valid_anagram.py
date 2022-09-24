class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count: dict[str, int] = {}
        for char in s:
            if char in s_count:
                s_count[char] += 1
            else:
                s_count[char] = 1

        t_count: dict[str, int] = {}
        for char in t:
            if char in t_count:
                t_count[char] += 1
            else:
                t_count[char] = 1

        if len(s_count) != len(t_count):
            return False

        for k, v in s_count.items():
            if t_count.get(k, None) != v:
                return False

        return True
