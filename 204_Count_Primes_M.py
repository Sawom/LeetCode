class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n

        is_prime[0] = False
        is_prime[1] = False

        i = 2
        while i*i < n:
            if is_prime[i]:
                for j in range(i*i,n,i):
                    is_prime[j]=False

            i=i+1

        prime_count = 0
        for p in is_prime:
            if p == True:
                prime_count = prime_count + 1

        return prime_count


if __name__ == "__main__":
    obj = Solution()
    print(obj.countPrimes(10))


"""
solution explanation:
class Solution:
    def countPrimes(self, n: int) -> int:
        # ০, ১ এবং ২ এর ছোট যেকোনো সংখ্যার জন্য প্রাইম সংখ্যা ০ টি
        if n <= 2:
            return 0
        
        # ধাপ ১: ০ থেকে n-1 পর্যন্ত একটি লিস্ট বানিয়ে সবাইকে True (প্রাইম) ধরে নিলাম
        is_prime = [True] * n
        
        # ০ এবং ১ প্রাইম সংখ্যা নয়, তাই এদের False করে দিলাম
        is_prime[0] = False
        is_prime[1] = False
        
        # ধাপ ২: ২ থেকে শুরু করে sqrt(n) পর্যন্ত কাটাকাটি চালাবো
        # (i * i < n মানেই হলো i < sqrt(n))
        i = 2
        while i * i < n:
            # যদি i সংখ্যাটি অক্ষত (True) থাকে, তবে এটি একটি প্রাইম নম্বর
            if is_prime[i]:
                
                # এবার i এর সব গুণিতককে (Multiples) কেটে False বানিয়ে দেব
                # লুপটি i*i থেকে শুরু করে n পর্যন্ত i করে লাফাবে (যেমন: 4, 6, 8, 10...)
                for j in range(i * i, n, i):
                    is_prime[j] = False
            
            # পরের সংখ্যায় যাওয়া
            i += 1
            
        # ধাপ ৩: লিস্টে কয়টি True বেঁচে আছে তা গুনে উত্তর দিয়ে দেব
        prime_count = 0
        for p in is_prime:
            if p == True:
                prime_count += 1
                
        return prime_count
"""