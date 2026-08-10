class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i>=0 or j>= 0 or carry:
            digit_a = int(a[i]) if i>=0 else 0
            digit_b = int(b[j]) if j>=0 else 0

            total = digit_a + digit_b + carry
            result.append(str(total%2))
            carry = total // 2

            i = i-1
            j = j-1

        return "".join(reversed(result))


if __name__ == "__main__":
    obj = Solution()
    a = "1010"
    b = "1011"
    print(obj.addBinary(a,b))

"""
solution explanation:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1  # a-এর একদম শেষের ইনডেক্স
        j = len(b) - 1  # b-এর একদম শেষের ইনডেক্স
        carry = 0
        res = []        # ফাস্ট পারফর্মেন্সের জন্য লিস্ট

        while i >= 0 or j >= 0 or carry:
            [দুটি স্ট্রিংয়ের দৈর্ঘ্য যদি সমান না হয়, তবে যেন কোনো এরর না আসে এবং অনুপস্থিত বিটের মানকে ০ হিসেবে ধরা যায়]
            digit_a = int(a[i]) if i >= 0 else 0 
            digit_b = int(b[j]) if j >= 0 else 0

            total = digit_a + digit_b + carry

            res.append(str(total % 2)) # O(1) টাইমে লিস্টে যুক্ত হবে
            carry = total // 2

            i -= 1
            j -= 1

        # লিস্টকে উল্টে একসাথে স্ট্রিং বানিয়ে নেওয়া
        return "".join(reversed(res))

"""