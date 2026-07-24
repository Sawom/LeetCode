from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s)-1

        while left < right:
            s[left] , s[right] = s[right] , s[left]
            left = left + 1
            right = right - 1

# run in pc
if __name__ == "__main__":
    obj = Solution()
    s = ["h", "e", "l", "l", "o"]
    print("Original List:", s)

    obj.reverseString(s)
    print("Reversed List:", s)
 
# explain   
# পাইথনে সাধারণ স্ট্রিং (যেমন: "hello") কিন্তু পরিবর্তন করা যায় না (Immutable)। কিন্তু লিটকোড ৩৪৪-এ ইনপুট হিসেবে কী দেওয়া হয়েছে খেয়াল করো:
# s = ["h","e","l","l","o"]
# 
# ওরা ইনপুট দিয়েছে ক্যারেক্টারের একটি লিস্ট (List of Characters)! আর পাইথনে লিস্টই হলো অ্যারে। অর্থাৎ, তোমাকে প্রতিটি অক্ষরকে এক একটি এলিমেন্ট
# হিসেবে একটা লিস্টের ভেতরেই দিয়ে দিয়েছে। তাই এটা মূলত একটা অ্যারে রিভার্স করারই প্রবলেম!