from typing import Dict, List


class Solution:
    # Time complexity O(n)
    # Space complexity O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tab: Dict[int, int] = {}

        for i, val in enumerate(nums):
            idx = tab.get(target - val)
            if idx is not None:
                return [idx, i]
            else:
                tab[val] = i

        return [0, 0]

    # Time complexity O(n^2)
    def twoSum_slow(self, nums: List[int], target: int) -> List[int]:
        for i, val_i in enumerate(nums[:-1]):
            for j in range(i + 1, len(nums)):
                if val_i + nums[j] == target:
                    return [i, j]

        return [0, 0]
