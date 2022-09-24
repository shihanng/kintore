import pytest
from valid_anagram import Solution


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("anagram", "nagaram", True),
        ("cat", "rat", False),
    ],
)
def test_is_anagram(s, t, expected):
    actual = Solution().isAnagram(s, t)
    assert expected == actual
