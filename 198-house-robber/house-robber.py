class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        -- Each possible house have two options, either we steal it or we skip it
        """
        N = len(nums)
        # dp[i] = max amount after stealing till ith house
        # len(dp) = N + 1
        dp = [-1] * (N + 1)
        
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, N+1):
            # if we teal the ith house, the max amount robbed
            # would be max amount till the last house + the amount of current house 
            # amount of current house is nums[i-1]
            steal = nums[i-1] + dp[i-2]

            # If we skip the total/max would be the amount robbed till the last house
            skip = dp[i-1]

            dp[i] = max(steal, skip)
        return dp[N]