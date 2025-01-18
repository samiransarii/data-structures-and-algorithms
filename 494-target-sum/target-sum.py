class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        
        def solve(idx, currSum):
            if idx >= n:
                return 1 if currSum == target else 0

            if (idx, currSum) in memo:
                return memo[(idx, currSum)]

            # + sign before the current element
            add = solve(idx + 1, currSum + nums[idx])

            # - sign before the current element
            subtract = solve(idx + 1, currSum - nums[idx])

            memo[(idx, currSum)] = add + subtract
            return memo[(idx, currSum)]

        numOfExpressions = solve(0, 0)
        return numOfExpressions