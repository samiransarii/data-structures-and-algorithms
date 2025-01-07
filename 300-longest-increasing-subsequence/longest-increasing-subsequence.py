class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N

        maxLIS = 1
        for i in range(N - 1, -1, -1):
            for j in range(i+1, N):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    maxLIS = max(maxLIS, dp[i])

        return maxLIS