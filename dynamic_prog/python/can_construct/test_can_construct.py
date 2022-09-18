import can_construct
import pytest


@pytest.mark.parametrize(
    "target,words,expected",
    [
        ("abcdef", ["ab", "abc", "cd", "def", "abcd"], True),
        ("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], False),
        ("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], True),
        (
            "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
            ["e ", "ee", "eee", "eeee", "eeeee", "eeeeee"],
            False,
        ),
    ],
)
def test_can_sum(target, words, expected):
    actual = can_construct.can_construct(target, words, memo={})
    assert expected == actual
