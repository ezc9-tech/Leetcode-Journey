class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We want to keep track of the numbers and indexes we already iterated over
        #this requires a hashmap
        hashmap = {}

        #For this problem we want to keep up with the indexes and numbers we are currently on
        #To do that we will use enumerate
        for index, num in enumerate(nums):
            #If the target - num is in hashmap then we found our match
            if target - num in hashmap:
                #We simply need to return the list of the prev index and current index of our match
                return [hashmap[target-num], index]
            #If it wasn't a match then we just record the num and its index in the hashmap
            hashmap[num] = index

            