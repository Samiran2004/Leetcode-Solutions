class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        # Calculate left Sum
        leftSum = [0]
        for i in range(0, len(nums) - 1):
            currSum = leftSum[-1] + nums[i]
            leftSum.append(currSum)
        
        def getRightSum(nums):
            totalSum = sum(nums)
            rightSum = []

            for num in nums:
                totalSum -= num
                rightSum.append(totalSum)
            return rightSum
        
        rightSum = getRightSum(nums)

        ans = []

        for i in range(len(nums)):
            currDiff = abs(leftSum[i] - rightSum[i])
            ans.append(currDiff)
        
        return ans