class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return n == 1

if __name__ == "__main__":
    obj = Solution()
    print(obj.isHappy(19))
    print(obj.isHappy(14))

"""
solution explanation:
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        # যতক্ষণ n এর মান 1 না হচ্ছে এবং আমরা অসীম লুপে না পড়ছি
        while n != 1 and n not in seen:
            seen.add(n)
            # ডিজিটের স্কয়ারের যোগফল বের করা
            n = sum(int(digit) ** 2 for digit in str(n))

        return n == 1


loop explanation:       n = sum(int(digit) ** 2 for digit in str(n))

 ধরো n = 19। 
 এই লাইনটি রান করার সময় পাইথন ভেতরের দিক থেকে বাইরের দিকে ধাপে ধাপে কাজ করে:
 ১ম ধাপ: str(n)
 পাইথন প্রথমে $19$ সংখ্যাটিকে স্ট্রিংয়ে রূপান্তর করে "19" বানায়।(কারণ স্ট্রিং বানালে এর প্রতিটি ক্যারেক্টারকে একটা একটা করে আলাদা করা যায়।)
 
 ২য় ধাপ: for digit in str(n)
 এবার লুপটি স্ট্রিং থেকে এক এক করে ক্যারেক্টারগুলো তুলে আনে:
 ১ম বারে পায়: digit = "1",  ২য় বারে পায়: digit = "9"
 
 ৩য় ধাপ: int(digit) ** 2 
 ক্যারেক্টারগুলোকে ইনটিজারে কনভার্ট করে তার বর্গ (Square) নির্ণয় করা হয়:
 ১ম ক্যারেক্টারের জন্য: int("1") ** 2 => 1^2 = 1 
 ২য় ক্যারেক্টারের জন্য: int("9") ** 2 => 9^2 = 81
 এখন পাইথনের হাতে দুটি মান প্রস্তুত: (1, 81)
 ৪র্থ ধাপ: sum(...)
 sum() ফাংশনটি ব্র্যাকেটের ভেতরের এই বর্গ করা মানগুলোকে একসাথে যোগ করে দেয়: 1 + 81 = 82
 ৫ম ধাপ: n = ...সবশেষে এই যোগফল 82-কে নতুন মান হিসেবে n ভ্যারিয়েবলে স্টোর/আপডেট করে দেওয়া হয় (n = 82)।
"""