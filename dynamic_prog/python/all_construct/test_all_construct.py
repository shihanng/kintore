import all_construct
import pytest


@pytest.mark.parametrize(
    "target,words,expected",
    [
        (
            "purple",
            ["purp", "p", "ur", "le", "purl"],
            [["purp", "le"], ["p", "ur", "p", "le"]],
        ),
        (
            "abcdef",
            ["ab", "abc", "cd", "def", "abcd", "ef", "c"],
            [
                ["ab", "cd", "ef"],
                ["ab", "c", "def"],
                ["abc", "def"],
                ["abcd", "ef"],
            ],
        ),
        ("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], []),
        (
            "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
            ["e ", "ee", "eee", "eeee", "eeeee", "eeeeee"],
            [],
        ),
    ],
)
def test_all_construct(target, words, expected):
    actual = all_construct.all_construct(target, words, memo={})
    assert expected == actual

    if target != "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef":
        actual = all_construct.all_construct_tab(target, words)
        assert {(frozenset(item)) for item in expected} == {
            (frozenset(item)) for item in actual
        }
