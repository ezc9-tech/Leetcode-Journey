class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #We will want the occurenses of each num which calls for a hashmap
        hashmap = {}
        
        #Lets loop through and grab all occurences of each element and put that into the hashmap
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        #Create a list of keys that is reverse sorted based on occurences
        most_occured = [key for key, value in sorted(hashmap.items(), key = lambda item: item[1], reverse=True)]
        
        #Retun k number of keys
        return most_occured[0:k]