from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

if __name__ == "__main__":
    arr1 = [2, 4, 3]
    arr2 = [5, 6, 4]

    l1 = ListNode(arr1[0])
    l1.next = ListNode(arr1[1])
    l1.next.next = ListNode(arr1[2])

    l2 = ListNode(arr2[0])
    l2.next = ListNode(arr2[1])
    l2.next.next = ListNode(arr2[2])

    obj = Solution()
    result_head = obj.addTwoNumbers(l1, l2)

    result_list = []
    curr = result_head
    while curr:
        result_list.append(curr.val)
        curr = curr.next

    print(f"Input: l1 = {arr1}, l2 = {arr2}")
    print(f"Output: {result_list}")

"""
solution explanation:
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # রেজাল্ট লিস্ট তৈরির জন্য ডামি নোড
        current = dummy      # নতুন নোড বসানোর পয়েন্টার
        carry = 0            # হাতের ১ ট্র্যাক রাখার ভেরিয়েবল

        # লুপ চলবে যতক্ষণ l1 বা l2 তে মান থাকবে, অথবা হাতে carry থাকবে
        while l1 or l2 or carry:
            # l1 এবং l2 এর মান থাকলে নেব, না থাকলে 0 ধরব
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # ৩টি মানের যোগফল
            total = val1 + val2 + carry

            # নতুন carry এবং নোডে বসানোর ডিজিট বের করা
            carry = total // 10
            digit = total % 10

            # নতুন নোড বানিয়ে লিংকড লিস্টে যুক্ত করা
            current.next = ListNode(digit)
            current = current.next

            # l1 এবং l2 কে এক ঘর সামনে এগিয়ে দেওয়া
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # dummy.next হলো আমাদের আসল রেজাল্ট লিস্টের হেড
        return dummy.next
"""
