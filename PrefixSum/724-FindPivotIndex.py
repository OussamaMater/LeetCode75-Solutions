"""
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
"""


class Solution:
    def pivotIndex(self, nums: list[int]) -> list[int]:
        leftSum = 0
        arraySum = sum(nums)

        for i in range(len(nums)):
            rightSum = arraySum - nums[i] - leftSum
            if leftSum == rightSum:
                return i

            leftSum += nums[i]

        return -1


# Running TestCase
solution = Solution()
print(solution.pivotIndex([1, 7, 3, 6, 5, 6]))
