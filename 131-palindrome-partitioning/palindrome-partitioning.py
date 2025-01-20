class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        output = []
        memo = {}

        def isPalindrome(start, end):
            if (start, end) in memo:
                return memo[(start, end)]

            left, right = start, end
            while left <= right:
                if s[left] != s[right]:
                    memo[(start, end)] = False
                    return False
                left += 1
                right -= 1
            
            memo[(start, end)] = True
            return True
            # memo[string] = string == string[::-1]
            # return memo[string]

        def solve(idx, currpath):
            if idx >= n:
                output.append(currpath[:])
                return
            
            for i in range(idx, n):
                substring = s[idx:i+1]
                if isPalindrome(idx, i):
                    currpath.append(substring)
                    solve(i + 1, currpath)
                    currpath.pop()


        solve(0, [])
        return output