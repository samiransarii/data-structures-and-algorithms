class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [-1] * (N)

        def solve(idx):
            if idx == N:
                return 0

            if dp[idx] != -1:
                return dp[idx]

            max_len = 1
            for next_idx in range(idx + 1, N):
                if nums[next_idx] > nums[idx]:
                    max_len = max(max_len, 1 + solve(next_idx))

            dp[idx] = max_len
            return dp[idx]

        # Compute the LIS considering all possible starting points
        return max(solve(i) for i in range(N))
