class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = [] 

        def findCombinations(i, curr):
            if len(curr) == k:
                output.append(curr.copy())
                return
            
            if i > n:
                return

            curr.append(i)

            findCombinations(i + 1, curr)

            curr.pop()

            findCombinations(i + 1, curr)
        
        findCombinations(1, [])
        return output

        