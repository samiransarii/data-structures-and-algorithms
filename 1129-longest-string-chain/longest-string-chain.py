class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        N = len(words)
        words = sorted(words, key=len)

        dp = [1] * N

        def isPredecessor(wordA, wordB):
            lenA, lenB = len(wordA), len(wordB)

            if lenA + 1 != lenB:
                return False

            a, b = 0, 0
            mismatched = False
            while b < lenB and a < lenA:
                if wordA[a] == wordB[b]:
                    a += 1
                    b += 1
                elif wordA[a] != wordB[b]:
                    if mismatched:
                        return False
                    mismatched = True
                    b += 1
            return True
        
        longestStringChain = 1
        for i in range(N):
            for j in range(i):
                if isPredecessor(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
                    longestStringChain = max(longestStringChain, dp[i])

        return longestStringChain
