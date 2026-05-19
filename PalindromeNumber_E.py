class Solution:
    def isPalindrome(self, x: int) -> bool:
        num , reverse = x, 0
        # checking if negetive
        if x<0:
            return False

        while x!=0:
            reverse = (reverse*10)+(x%10)
            x=x//10

        if reverse==num:
            return True
        else:
            return False

# ide run
if __name__ == "__main__":
    obj = Solution()
    x= -121
    print(obj.isPalindrome(x))

