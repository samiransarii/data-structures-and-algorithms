class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        N = len(words)
        sortedWords = sorted(words, key=len)
        dp = [[''] * (N + 1) for _ in range(N)]

        def isPredecessor(wordA, wordB):
            lenA, lenB = len(wordA), len(wordB)
            if lenA + 1 != lenB:
                return False

            a, b = 0, 0
            while b < lenB and a < lenA:
                if wordA[a] == wordB[b]:
                    a += 1
                b += 1
            return a == lenA
        
        def solve(idx, prev):
            if idx >= N:
                return 0

            if dp[idx][prev] != '':
                return dp[idx][prev]

            wordA = sortedWords[prev]
            wordB = sortedWords[idx]
            take = 0
            if prev == -1 or isPredecessor(wordA, wordB):
                take = 1 + solve(idx + 1, idx)
            
            skip = solve(idx + 1, prev)

            if prev != -1:
                dp[idx][prev] = max(take, skip)
            return dp[idx][prev] if prev != -1 else max(take, skip)

        output = solve(0, -1)
        return output

