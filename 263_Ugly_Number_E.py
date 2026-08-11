class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False

        for p in [2,3,5]:
            while n%p==0:
                n=n//p

        return n==1

if __name__ == "__main__":
    obj = Solution()
    print(obj.isUgly(6))
    print(obj.isUgly(14))

"""
solution explanation:
class Solution:
    def isUgly(self, n: int) -> bool:
        # ঋণাত্মক সংখ্যা বা ০ Ugly Number হতে পারে না
        if n <= 0:
            return False

        # ২, ৩ এবং ৫ দিয়ে যতবার সম্ভব ভাগ করব
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p

        # সব ২, ৩, ৫ সরানোর পর যদি ১ থাকে তবেই True
        return n == 1
"""