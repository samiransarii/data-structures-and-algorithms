class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        totalSubsets = 0
        memo = {}

        def findNumberOfBeautifulSubsets(idx, visited):
            nonlocal totalSubsets

            if idx >= n:
                return 1

            key = (idx, tuple(sorted(visited.keys())))
            if key in memo:
                return memo[key]

            # Not take
            noTake = findNumberOfBeautifulSubsets(idx + 1, visited)

            # Take
            take = 0
            if (nums[idx] - k) not in visited and (nums[idx] + k) not in visited:
                # Add to the current subset
                visited[nums[idx]] += 1
                take += findNumberOfBeautifulSubsets(idx + 1, visited)

                # Remove from the current subset
                visited[nums[idx]] -= 1
                if visited[nums[idx]] == 0:
                    del visited[nums[idx]]

            memo[key] = take + noTake
            return memo[key]


        totalSubsets = findNumberOfBeautifulSubsets(0, collections.defaultdict(int))
        return totalSubsets - 1