class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n

        first = 1
        second = 2

        for i in range (3, n+1):
            third = first + second
            first = second
            second = third

        return second

if __name__ == "__main__":
    obj = Solution()
    print(obj.climbStairs(5))

"""
solution explanation:
এই কোডটির মূল উদ্দেশ্য হলো—১ বা ২ ধাপ লাফিয়ে $n$-তম সিঁড়িতে পৌঁছানোর মোট কতগুলো ভিন্ন উপায় (Ways) আছে তা হিসাব করা।
যেহেতু প্রতিটি সিঁড়িতে পৌঁছানোর উপায় হলো তার আগের দুটি সিঁড়ির উপায়ের যোগফল ($\text{Ways}(n) = \text{Ways}(n-1) + \text{Ways}(n-2)$), 
তাই কোডটিতে খুব দক্ষতার সাথে ফিবোনাক্কি সিরিজের লজিক ব্যবহার করা হয়েছে।

class Solution:
    def climbStairs(self, n: int) -> int:
        # ১ ও ২ নম্বর সিঁড়ির জন্য উত্তর যথাক্রমে ১ ও ২
        if n <= 2:
            return n

        first = 1   # ১ নম্বর সিঁড়িতে পৌঁছানোর মোট উপায়
        second = 2  # ২ নম্বর সিঁড়িতে পৌঁছানোর মোট উপায়

        # ৩ নম্বর সিঁড়ি থেকে n পর্যন্ত হিসাব করব
        for i in range(3, n + 1):
            third = first + second  # বর্তমান সিঁড়ি = আগের ২ সিঁড়ির উপায়ের যোগফল
            first = second          # first কে ১ ঘর সামনে পাঠালাম
            second = third          # second কে ১ ঘর সামনে পাঠালাম

        return second  # n-তম সিঁড়ির চূড়ান্ত মান এখন second-এ আছে
"""