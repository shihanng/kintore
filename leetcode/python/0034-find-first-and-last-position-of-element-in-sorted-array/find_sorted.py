from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        return [find_start(nums, target), find_end(nums, target)]


def find_start(nums: List[int], target: int) -> int:
    if nums[0] == target:
        return 0

    left = 0
    right = len(nums) - 1

    while left <= right:
        m = (left + right) // 2

        if nums[m] == target and nums[m - 1] < nums[m]:
            return m

        if target <= nums[m]:
            right = m - 1
        else:
            left = m + 1

    return -1


def find_end(nums: List[int], target: int) -> int:
    if nums[-1] == target:
        return len(nums) - 1

    left = 0
    right = len(nums) - 1

    while left <= right:
        m = (left + right) // 2

        if nums[m] == target and nums[m + 1] > nums[m]:
            return m

        if target >= nums[m]:
            left = m + 1
        else:
            right = m - 1

    return -1
