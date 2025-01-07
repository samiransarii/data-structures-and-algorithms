class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        N = len(nums)
        
        dp = [[-1] * 2 for _ in range(N)]
        def solve(idx, isEven):
            if idx >= N:
                return 0

            if dp[idx][isEven] != -1:
                return dp[idx][isEven]

            # skip the current element
            skip = solve(idx + 1, isEven)

            val = nums[idx]
            val = val if isEven else -val

            take = solve(idx + 1, not isEven) + val

            dp[idx][isEven] = max(skip, take)
            return dp[idx][isEven]

        output = solve(0, True)
        return output

