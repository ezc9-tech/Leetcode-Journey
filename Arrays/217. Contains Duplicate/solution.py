class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #We are looking for duplicates which is perfect for a set/hashset
        #I just named this hashset because I needed something other than set lol
        hashset = set()
        
        #We are going to iterate through the list
        for num in nums:
            #If the number we are currently on is not in the hashset
            if num not in hashset:
                #add it to the hashset
                hashset.add(num)
            else:
                #else return true that there is a duplicate
                return True
        #lastly if there are no duplicates return false
        return False