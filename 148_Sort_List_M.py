from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        values.sort()

        current = head
        for val in values:
            current.val = val
            current = current.next

        return head


if __name__ == "__main__":
    obj = Solution()
    raw_list = [-1, 5, 3, 4, 0]

    head = ListNode(raw_list[0])
    current = head
    for val in raw_list[1:]:
        current.next = ListNode(val)
        current = current.next

    sorted_head = obj.sortList(head)

    result = []
    curr = sorted_head
    while curr:
        result.append(curr.val)
        curr = curr.next

    print(result)

"""
solution explanation:
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # ১. লিঙ্কড লিস্টের সব মান পাইথন লিস্টে জমা করি - O(N)
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        # ২. পাইথনের সর্টিং চালাই - O(N log N)
        values.sort()

        # ৩. সর্ট করা মানগুলো আবার লিঙ্কড লিস্টের নোডে ফেরত বসাই - O(N)
        curr = head
        for val in values:
            curr.val = val
            curr = curr.next

        return head
"""