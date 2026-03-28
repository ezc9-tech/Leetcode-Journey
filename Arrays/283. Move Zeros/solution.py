class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Keep track of the 0's
        l = 0
        #Find all non-zeros within nums
        for r in range(len(nums)):
            #If you find a non-zero
            if nums[r]:
                #Swap the non-zero with the zero value
                nums[l], nums[r] = nums[r], nums[l]
                #Then iterate your left pointer to another zero
                l += 1