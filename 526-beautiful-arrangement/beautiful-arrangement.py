class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0

        def isBeautifulArrangement(currpath):
            for idx, num in enumerate(currpath):
                if (idx + 1) % num != 0 and num % (idx + 1) != 0:
                    return False

            return True
       
        def findPermutations(pos, visited):
            nonlocal count

            if pos > n:
                count += 1
                return

            for num in range(1, n + 1):
                if num not in visited and (pos % num == 0 or num % pos == 0):
                    visited.add(num)
                    findPermutations(pos + 1, visited)
                    visited.remove(num)
                    

        findPermutations(1, set())
        return count

        