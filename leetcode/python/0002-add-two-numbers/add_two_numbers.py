from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def new_list_node(digits: List[int]) -> Optional[ListNode]:
    nextNode = None
    for i in reversed(digits):
        nextNode = ListNode(i, nextNode)
    return nextNode


def parse_list_node(node: Optional[ListNode]) -> List[int]:
    parsed: List[int] = []

    while node:
        parsed.append(node.val)
        node = node.next

    return parsed


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ans = ListNode()
        next = ans
        carry = 0

        while l1 is not None or l2 is not None:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            if sum >= 10:
                sum = sum - 10
                carry = 1
            else:
                carry = 0

            digit = ListNode(sum)

            next.next = digit

            next = digit

        if carry:
            next.next = ListNode(carry)

        return ans.next
