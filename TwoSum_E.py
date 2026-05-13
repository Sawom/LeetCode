from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store_number = {}

        for i,n in enumerate(nums):
            difference = target - n

            if difference in store_number:
                return [store_number[difference],i]

            else:
                store_number[n] = i

        return []

# test case code run
if __name__ == "__main__":
    obj= Solution()

    test_num = [2,7,11,15]
    test_target = 22

    result = obj.twoSum(test_num, test_target)

    print(f"output: {result}")
