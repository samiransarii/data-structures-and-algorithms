class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        output = []

        def isPalindrome(string):
            return string == string[::-1]

        def solve(idx, currpath):
            if idx >= n:
                output.append(currpath[:])
                return
            
            for i in range(idx, n):
                substring = s[idx:i+1]
                if isPalindrome(substring):
                    currpath.append(substring)
                    solve(i + 1, currpath)
                    currpath.pop()


        solve(0, [])
        return output