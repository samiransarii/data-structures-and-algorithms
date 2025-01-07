class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1:
            return nums[0]

        dp = [0] * (N + 1)
        dp[0] = 0

        for i in range(1, N):
            steal = nums[i - 1] + (dp[i - 2] if i - 2 >= 0 else 0)
            skip = dp[i - 1]

            dp[i] = max(steal, skip)

        output1 = dp[N-1]

        dp = [0] * (N + 1)
        dp[0] = 0

        for i in range(2, N+1):
            steal = nums[i - 1] + (dp[i - 2] if i - 2 >= 0 else 0)
            skip = dp[i - 1]

            dp[i] = max(steal, skip)

        output2 = dp[N]

        return max(output1, output2)


        