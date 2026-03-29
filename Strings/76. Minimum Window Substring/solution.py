class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #If t is empty, return empty string
        if t == "":
            return ""
        
        #Keep track of our current window and the count of T that we need to meet
        countT, window = {}, {}

        #Get a complete count of T
        for c in t:
            if c not in countT:
                countT[c] = 1
            else:
                countT[c] += 1
        
        #Keep track of how many characters we currently have and how many we need
        have, need = 0, len(countT)
        #Keep track of our result indexes and the length of that result
        res, resLen = [-1, -1], float("infinity")

        #We need a left and right pointer for sliding window problems
        l = 0
        #For the right pointer we will loop through every index of s
        for r in range(len(s)):
            #Lets get the current character
            c = s[r]
            #Add that character to our current window count
            window[c] = 1 + window.get(c, 0)
            
            #If that character is in countT and we have the same amount in our current window
            if c in countT and window[c] == countT[c]:
                #Then iterate have by 1
                have += 1
            
            #Once have equals need, we should try to shrink the result
            while have == need:
                #If the current window is smaller than the current result
                if (r - l + 1) < resLen:
                    #Make result our current window
                    res = [l,r]
                    #Update the length of our result
                    resLen = (r - l + 1)
                #Reduce the number of the left character in our current window by 1
                window[s[l]] -= 1
                #If thhe character we just removed made our window not match countT
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    #Then we need to reduce have by 1
                    have -= 1
                #Shrink the left side of the window by 1
                l += 1
        #Res should equal the final result so we can make l and r equal to result
        l, r = res
        #Return the substring with the result indexes as long as resLen is not infinity, then return empty string
        return s[l:r+1] if resLen != float("infinity") else ""


