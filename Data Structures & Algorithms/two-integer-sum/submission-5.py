class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                print(i,j)
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]

                