class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Since this is finding a number, we should use binary search
        #So we need a left and right pointer
        l = 0
        r = len(nums) - 1

        #For this question if l = r that means we found the answer
        while l < r:
            #We need to find the middle
            m = l + (r-l) // 2
            #We need to check if the middle is less than the right, and move the left accordingly
            if nums[m] < nums[r]:
                r = m
            #Else we need to move the left to the middle + 1 because the middle isn't the answer
            else:
                l = m + 1
        #At this point once the loop is done running, l = r, and they should
        #be pointing at the minimum, so return nums[l] or nums[r]
        return nums[l]