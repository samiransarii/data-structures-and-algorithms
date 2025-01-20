class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the pivot element which is greater than its next element
        n = len(nums)
        pivot = -1
        
        for i in range(n - 1, -1, -1):
            if nums[i-1] < nums[i]:
                pivot = i - 1
                break

        if pivot != -1:    
            # find the swap element
            swapIdx = pivot
            for i in range(n - 1, pivot, -1):
                if nums[i] > nums[pivot]:
                    swapIdx = i
                    break

            # swap
            nums[pivot], nums[swapIdx] = nums[swapIdx], nums[pivot]
            nums[pivot+1:] = nums[pivot+1:][::-1]
        else:
            nums[:] = nums[:][::-1]