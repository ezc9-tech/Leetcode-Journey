class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Keep track of the k number of elements
        k = 0
        #Go through every element in nums
        for num in nums:
            #If the length of our kept elements is less than 2 or
            #if num is not equal to two elements back
            if k < 2 or num != nums[k - 2]:
                #change the k index to be num
                nums[k] = num
                #iterate k
                k += 1
        return k