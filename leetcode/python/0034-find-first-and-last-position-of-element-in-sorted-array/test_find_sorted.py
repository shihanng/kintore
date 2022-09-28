import pytest
from find_sorted import Solution


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([2, 2], 2, [0, 1]),
    ],
)
def test_searchRange(nums, target, expected):
    actual = Solution().searchRange(nums, target)
    assert expected == actual
