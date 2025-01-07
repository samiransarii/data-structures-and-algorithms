class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1:
            return nums[0]

        dp = [0] * N
        dp[0] = nums[0]

        for i in range(1, N-1):
            steal = nums[i] + (dp[i - 2] if i - 2 >= 0 else 0)
            skip = dp[i - 1]
            dp[i] = max(steal, skip)

        output1 = dp[N-2]

        dp = [0] * N
        dp[1] = nums[1]

        for i in range(2, N):
            steal = nums[i] + (dp[i - 2] if i - 2 >= 0 else 0)
            skip = dp[i - 1]
            dp[i] = max(steal, skip)

        output2 = dp[N-1]

        return max(output1, output2)