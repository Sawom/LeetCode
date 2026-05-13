from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)


# test code in ide
if __name__ == "__main__":
    obj = Solution()
    # user input
    nums = [int(x) for x in input('Enter numbers separated by space: ').split()]
    # nums = [1,2,3,5,6] or direct array
    result = obj.containsDuplicate(nums)

    if(result):
        print('true')
    else:
        print('false')
