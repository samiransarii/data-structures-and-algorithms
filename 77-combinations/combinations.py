class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = [] 

        def findCombinations(i, curr):
            if len(curr) == k:
                output.append(curr.copy())
                return
            
            if i > n:
                return

            for i in range(i, n+1):
                curr.append(i)
                findCombinations(i+1, curr)
                curr.pop()
        
        findCombinations(1, [])
        return output

        