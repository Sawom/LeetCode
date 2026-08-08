class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 1
        right = x // 2

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            if mid * mid < x:
                left = mid + 1

            else:
                right  = mid -1

        return right

if __name__ == "__main__":
    obj = Solution()
    print(obj.mySqrt(8))
    print(obj.mySqrt(81))
    print(obj.mySqrt(16))


"""
solution explanation:
class Solution:
    def mySqrt(self, x: int) -> int:
        # ০ এবং ১ এর বর্গমূল তারা নিজেরাই
        if x < 2:
            return x

        left = 1
        right = x // 2

        while left <= right:
            mid = (left + right) // 2

            # যদি নিখুঁত বর্গমূল পাওয়া যায়
            if mid * mid == x:
                return mid

            # যদি স্কয়ার ছোট হয়, তাহলে উত্তর ডানপাশে আছে
            if mid * mid < x:
                left = mid + 1
            # যদি স্কয়ার বড় হয়ে যায়, তাহলে উত্তর বামপাশে আছে
            else:
                right = mid - 1

        # লুপ শেষ হলে 'right' পয়েন্টারটিই সবসময় সঠিক পূর্ণসংখ্যা উত্তর ধারণ করে
        return right

"""