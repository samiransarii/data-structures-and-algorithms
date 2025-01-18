class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        length = len(s)
        maxCount = 0
        seen = set()

        def solve(idx, currCount):
            nonlocal maxCount

            if idx >= length:
                maxCount = max(maxCount, currCount)
                return currCount

            for j in range(idx, length):
                subString = s[idx:j+1]
                if subString not in seen:
                    seen.add(subString)
                    solve(j+1, currCount + 1)
                    seen.remove(subString)


        solve(0, 0)
        return maxCount
        