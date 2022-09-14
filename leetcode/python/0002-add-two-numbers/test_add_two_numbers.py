import pytest
from add_two_numbers import Solution, new_list_node, parse_list_node


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
def test_eval(l1, l2, expected):
    actual = Solution().addTwoNumbers(new_list_node(l1), new_list_node(l2))
    assert expected == parse_list_node(actual)
