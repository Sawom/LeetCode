class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        if n < 0:
            x = 1/x
            n = -n

        result = 1.0

        while n > 0:
            if n % 2 == 1:
                result = result * x

            x  = x*x
            n = n//2

        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.myPow(2.00000,10))

"""
solution explanation:
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # ১. পাওয়ার ০ হলে যেকোনো সংখ্যার উত্তর সবসময় ১.০ (যেমন: 2^0 = 1)
        if n == 0:
            return 1.0

        # ২. পাওয়ার নেগেটিভ হলে (যেমন: 2^-2), বেস উল্টে দেব (1/2 = 0.5) এবং পাওয়ার পজিটিভ করব (+2)
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0  # ফাইনাল উত্তর জমিয়ে রাখার জন্য ১.০ ধরে নিলাম

        # ৩. যতক্ষণ পাওয়ার ০ না হচ্ছে, বাইনারি এক্সপোনেনসিয়েশন লুপ চলবে
        while n > 0:
            # পাওয়ার বিজোড় হলে (যেমন: 5), একটা অতিরিক্ত x রেজাল্টের সাথে গুণ করে নেব
            if n % 2 == 1:
                result = result * x

            # প্রতি ধাপে বেসকে স্কয়ার করব (x = x^2) এবং পাওয়ার অর্ধেক (n = n // 2) করে কমিয়ে দেব
            # এর ফলে ওয়ান-বাই-ওয়ান গুণ না করে ও লগারিথমিক টাইমে (O(log n)) দ্রুত কাজ শেষ হয়
            x = x * x
            n = n // 2

        return result  # ফাইনাল ক্যালকুলেট করা উত্তর রিটার্ন      
"""
