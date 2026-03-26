class Solution:
    def isPalindrome(self, s: str) -> bool:
        #We need a left and right pointer for both ends of the string
        l, r = 0, len(s) - 1

        #Because we only need to check until l = r we can do this
        while l < r:
            #Get through all non alpha numeric characters
            while l < r and not s[l].isalnum():
                l += 1
            #Do the same on the right
            while l < r and not s[r].isalnum():
                r -= 1
            #Now you can compare to see if it is a valid palindrome
            if s[l].lower() != s[r].lower():
                return False
            #Iterate through the string
            l += 1
            r -= 1
        #If you make it out of the loop then it is valide
        return True
            