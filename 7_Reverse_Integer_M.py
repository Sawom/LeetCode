class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            is_negative = True
            x = -x
        else:
            is_negative = False

        reverseResult = 0

        while(x!=0):
            reverseResult = (reverseResult*10) + (x%10)
            x=x//10

        if is_negative:
            reverseResult = -reverseResult

        if reverseResult < -2 ** 31 or reverseResult > (2 ** 31 - 1):
            return 0

        return reverseResult


if __name__ == "__main__":
    obj = Solution()
    print(obj.reverse(123))
    print(obj.reverse(-123))
    print(obj.reverse(120))

"""
solution explanation:
class Solution:
    def reverse(self, x: int) -> int:
        # ১. নেগেটিভ সংখ্যা চেক করে মনে রাখা
        if x < 0:
            is_negative = True
            x = -x  # নেগেটিভ সংখ্যাকে পজিটিভ বানিয়ে নেওয়া (যাতে পাইথনের % ও // ঠিকমতো কাজ করে)
        else:
            is_negative = False

        reverseResult = 0

        # ২. সাধারণ পজিটিভ সংখ্যার জন্য ডিজিট রিভার্স করার লুপ
        while x != 0:
            digit = x % 10                        # শেষের শেষ ডিজিটটি কেটে নেওয়া
            reverseResult = (reverseResult * 10) + digit  # ডিজিটটি উল্টো সংখ্যার সাথে যোগ করা
            x = x // 10                           # শেষের ডিজিটটি মূল সংখ্যা থেকে ফেলে দেওয়া

        # ৩. আসল সংখ্যাটি যদি শুরুতে নেগেটিভ থেকে থাকে, তবে আবার নেগেটিভ বানিয়ে দেওয়া
        if is_negative:
            reverseResult = -reverseResult

        # ৪. ৩২-বিট সাইনড ইন্টিজার লিমিট চেক (-2^31 থেকে 2^31 - 1)
        # পাইথনে লিমিট ওভারফ্লো ধরা পড়ে না, তাই ম্যানুয়ালি চেক করে সীমা পার হলে 0 রিটার্ন করতে হয়
        if reverseResult < -2**31 or reverseResult > (2**31 - 1):
            return 0

        return reverseResult

"""