#Seoyoon Park

#1
def maxSubArrayDivideAndConquer(nums: list[int]) -> int:
    def findSubArray(nums, left, right):
        if left > right:
            return -10000
        
        mid = (left+right) // 2
        point = 0
        leftSum = 0
        rightSum = 0

        for i in range(mid-1, left-1, -1):
            point += nums[i]
            leftSum = max(leftSum, point)

        point=0
        for i in range(mid+1, right+1):
            point += nums[i]
            rightSum = max(rightSum, point)

        combinedSum = nums[mid] + leftSum + rightSum

        left_half = findSubArray(nums, left, mid-1)
        right_half = findSubArray(nums, mid+1, right)

        return max(combinedSum, left_half, right_half)

    return findSubArray(nums, 0, len(nums)-1)
        

#2
def maxSubArrayKadane(nums: list[int]) -> int:
    maxSum = -10000
    maxPoint = 0
    for i in range(0,len(nums)):
        maxPoint += nums[i]
        if(maxSum < maxPoint):
            maxSum = maxPoint
        if(maxPoint < 0):
            maxPoint = 0
    return maxSum







