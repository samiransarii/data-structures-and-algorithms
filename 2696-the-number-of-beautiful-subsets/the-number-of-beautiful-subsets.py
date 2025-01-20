class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        totalSubsets = 0
        visited = collections.defaultdict(int)

        def findNumberOfBeautifulSubsets(idx, visited):
            nonlocal totalSubsets

            if idx >= n:
                totalSubsets += 1
                return

            # Not take
            findNumberOfBeautifulSubsets(idx + 1, visited)

            # Take
            if (nums[idx] - k) not in visited and (nums[idx] + k) not in visited:
                # Add to the current subset
                visited[nums[idx]] += 1
                findNumberOfBeautifulSubsets(idx + 1, visited)

                # Remove from the current subset
                visited[nums[idx]] -= 1
                if visited[nums[idx]] == 0:
                    del visited[nums[idx]]

        findNumberOfBeautifulSubsets(0, visited)
        return totalSubsets - 1