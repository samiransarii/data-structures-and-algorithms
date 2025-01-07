class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        -- Each possible house have two options, either we steal it or we skip it
        """
        N = len(nums)
        dp = [-1] * N

        def solve(indx):
            if indx >= N:
                return 0

            if dp[indx] != -1:
                return dp[indx]

            steal = nums[indx] + solve(indx + 2)
            skip = solve(indx + 1)

            dp[indx] = max(steal, skip)
            return dp[indx]

        output = solve(0)
        return output
