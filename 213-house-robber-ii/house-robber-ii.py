class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        if N == 1:
            return nums[0]

        if N == 2:
            return max(nums[0], nums[1])

        def solve(indx, end, dp):
            if indx > end:
                return 0
            
            if dp[indx] != -1:
                return dp[indx]

            steal = nums[indx] + solve(indx + 2, end, dp)
            skip = solve(indx + 1, end, dp)

            dp[indx] = max(steal, skip)
            return dp[indx]

        dp = [-1] * N
        firstIndxOutput = solve(0, N - 2, dp)

        dp = [-1] * N
        secondIndxOutput = solve(1, N - 1, dp)

        return max(firstIndxOutput, secondIndxOutput)