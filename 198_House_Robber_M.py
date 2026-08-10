from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for i in nums:
            temp = max(i + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

if __name__ == "__main__":
    obj = Solution()
    nums = [7,1,2,9,1]
    print(obj.rob(nums))

"""
solution explanation:
class Solution:
    def rob(self, nums: list[int]) -> int:
        # rob1 = ২ ঘর আগের বাড়ি পর্যন্ত পাওয়া সর্বোচ্চ টাকা
        # rob2 = ১ ঘর আগের বাড়ি পর্যন্ত পাওয়া সর্বোচ্চ টাকা
        rob1 = 0  
        rob2 = 0  

        # প্রতিটি বাড়ির টাকার ওপর লুপ ঘুরবে
        for n in nums:
            # বর্তমান বাড়ির (n) জন্য ২টি বিকল্প তুলনা করা হচ্ছে:
            # বিকল্প ১ (n + rob1) : বর্তমান বাড়িতে চুরি করব + ১ ঘর স্কিপ দিয়ে তার আগের বাড়ির টাকা নেব
            # বিকল্প ২ (rob2)     : বর্তমান বাড়িতে চুরি করব না, ১ ঘর আগের সর্বোচ্চ টাকাই রেখে দেব
            temp = max(n + rob1, rob2)

            # মানগুলো ১ ঘর করে সামনে শিফট করা হচ্ছে (পরের লুপের জন্য)
            rob1 = rob2   # পুরোনো rob2 এখন হয়ে গেল rob1 (২ ঘর আগের মান)
            rob2 = temp   # নতুন বের হওয়া সর্বোচ্চ মানটি এখন rob2 (১ ঘর আগের মান)

        # লুপ শেষে সবকটি বাড়ি হিসাব করে পাওয়া চূড়ান্ত সর্বোচ্চ টাকা rob2-তে জমা থাকবে
        return rob2
"""