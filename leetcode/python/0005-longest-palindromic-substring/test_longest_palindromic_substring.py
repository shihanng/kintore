import pytest
from longest_palindromic_substring import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("babab", "babab"),
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("abacab", "bacab"),
    ],
)
def test_longest_palindrome(s, expected):
    actual = Solution().longestPalindrome(s)
    assert expected == actual
