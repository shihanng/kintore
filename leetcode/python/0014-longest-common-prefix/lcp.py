from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i, common_prefix = 0, ""

        while i <= len(strs[0]):
            first_str = strs[0][:i]
            for s in strs[1:]:
                if i > len(s):
                    return common_prefix

                if s[:i] != first_str:
                    return common_prefix

            common_prefix = first_str
            i = i + 1

        return common_prefix
