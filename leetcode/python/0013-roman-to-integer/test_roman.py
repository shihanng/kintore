import pytest
from roman import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("I", 1),
        ("II", 2),
        ("XII", 12),
        ("XXVII", 27),
        ("IV", 4),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ],
)
def test_romanToInt(s, expected):
    actual = Solution().romanToInt(s)
    assert actual == expected
