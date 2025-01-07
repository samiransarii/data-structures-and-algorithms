class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        N = len(nums)
        
        # dp[[-1, -1]] for even and odd length subsequence
        # dp[idx][0] for even length
        # dp[idx][1] for odd length
        dp = [[0] * 2 for _ in range(N + 1)]

        for i in range(1, N+1):

            # Even length subsequence till index i means the index will be odd so subtract
            dp[i][0] = max(dp[i-1][1] - nums[i-1], dp[i-1][0])

            # Odd length subsequence till index i means the index will be even so add
            dp[i][1] = max(dp[i-1][0] + nums[i-1], dp[i-1][1])

        output = max(dp[N][0], dp[N][1])
        return output