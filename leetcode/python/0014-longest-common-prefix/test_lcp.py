import pytest
from lcp import Solution


@pytest.mark.parametrize(
    "strs,expected",
    [
        (["flower", "flow", "flight"], "fl"),
        (["abc", "abc", "abc"], "abc"),
        (["dog", "racecar", "car"], ""),
    ],
)
def test_longestCommonPrefix(strs, expected):
    actual = Solution().longestCommonPrefix(strs)
    assert expected == actual
