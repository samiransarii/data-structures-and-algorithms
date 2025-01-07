class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        N = len(nums)
        
        dp = [[-1] * 2 for _ in range(N)]

        # flag -> True means even idx (Boolean: 1)
        # flag -> False means odd idx (Boolean: 0)
        def solve(idx, flag):
            if idx >= N:
                return 0

            if dp[idx][flag] != -1:
                return dp[idx][flag]

            # skip the current element
            skip = solve(idx + 1, flag)

            val = nums[idx]
            val = val if flag else -val

            take = solve(idx + 1, not flag) + val

            dp[idx][flag] = max(skip, take)
            return dp[idx][flag]

        output = solve(0, True)
        return output

