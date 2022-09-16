import pytest
from palindrome_number import Solution


@pytest.mark.parametrize(
    "x,expected",
    [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
    ],
)
def test_isPalindrome(x, expected):
    actual = Solution().isPalindrome(x)
    assert expected == actual
