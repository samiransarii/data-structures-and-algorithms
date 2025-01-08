class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        N, M, K = n, m + 1, k
        MOD = 10**9 + 7
        
        dp = [[[-1 for _ in range(101)] for _ in range(51)] for _ in range(51)]

        def solve(idx, searchCost, maxSoFar):
            if idx >= N:
                if searchCost == K:
                    return 1
                return 0

            if dp[idx][searchCost][maxSoFar] != -1:
                return dp[idx][searchCost][maxSoFar]

            result = 0
            for i in range(1, M):
                if i > maxSoFar:
                    result += solve(idx + 1, searchCost + 1, i) % MOD
                else:
                    result += solve(idx + 1, searchCost, maxSoFar) % MOD

            result %= MOD
            dp[idx][searchCost][maxSoFar] = result
            return result

        output = solve(0, 0, 0)
        return output