# House Robber Problem
# Solved by Abdul Nawab
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:  # No houses
            return 0
        if n == 1:  # Only one house, rob it
            return nums[0]
        if n == 2:  # Two houses, rob the richer one
            return max(nums[0], nums[1])
        # Initialize the dp array to store the max amount robbed up to each house
        dp = [0] * n
        dp[0] = nums[0]  # Rob the first house
        dp[1] = max(nums[0], nums[1])  # Rob the richer of the first two houses
        # Process the rest of the houses
        for i in range(2, n):
        # Either rob this house and add to the amount from dp[i-2], or skip this house
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        maxSum = max(dp)
        # The last element of dp will have the maximum amount of money that can be robbed
        return maxSum

# Notes
# [1, 1, 3, 3]
# [0, 0, 0, 0] <- DP Array

# Right before the for loop
# DP = [1, 1,  ..., ....]

# Then, we step into our for loop
# And we populate our DP array
# DP = [1, 1, 4, 4]
# And what you are going to do is return the last element. Or max