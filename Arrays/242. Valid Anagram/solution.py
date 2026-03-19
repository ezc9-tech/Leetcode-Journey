class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #If the two strings are not the same length
        if len(s) != len(t):
            #return false because they can't be anagrams
            return False
        
        #we are looking for occurences of characters which calls for a hashmap
        s_hashmap = {}

        #for each character in this string
        for char in s:
            #if it isn't in the hashmap then set its occurences equal to one
            if char not in s_hashmap:
                s_hashmap[char] = 1
            #else add 1 to its current occurences
            else:
                s_hashmap[char] += 1

        #do the same thing for the other string
        t_hashmap = {}

        for char in t:
            if char not in t_hashmap:
                t_hashmap[char] = 1
            else:
                t_hashmap[char] += 1

        #return true if each hashmap is the same because they are anagrams
        #else return false
        return s_hashmap == t_hashmap


        