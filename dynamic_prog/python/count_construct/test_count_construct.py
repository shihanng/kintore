import count_construct
import pytest


@pytest.mark.parametrize(
    "target,words,expected",
    [
        ("purple", ["purp", "p", "ur", "le", "purl"], 2),
        ("abcdef", ["ab", "abc", "cd", "def", "abcd"], 1),
        ("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], 0),
        ("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], 4),
        (
            "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
            ["e ", "ee", "eee", "eeee", "eeeee", "eeeeee"],
            0,
        ),
    ],
)
def test_count_construct(target, words, expected):
    actual = count_construct.count_construct(target, words, memo={})
    assert expected == actual

    actual = count_construct.count_construct_tab(target, words)
    assert expected == actual
