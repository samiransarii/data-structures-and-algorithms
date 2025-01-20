class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        memo = {}
       
        def findPermutations(pos, visited):
            nonlocal count
            if pos > n:
                return 1

            state = (pos, str(visited))
            if state in memo:
                return memo[state]

            count = 0
            for num in range(1, n + 1):
                if num not in visited and (pos % num == 0 or num % pos == 0):
                    visited.add(num)
                    count += findPermutations(pos + 1, visited)
                    visited.remove(num)

            memo[state] = count
            return count

        findPermutations(1, set())
        return count
        