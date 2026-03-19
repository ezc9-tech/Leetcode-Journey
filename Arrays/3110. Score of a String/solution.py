class Solution:
    def scoreOfString(self, s: str) -> int:
        #We will use a left pointer to keep up with the first number
        l = 0

        #Need to keep track of the total score
        total = 0
        
        #Then the right pointer will be the char
        for char in s[1::]:
            #As we iterate through the list add the absolute value of the left ascii value
            #minus the right ascii value to total
            total += (abs(ord(s[l]) - ord(char)))
            #Make sure to iterate the left pointer as well
            l += 1
        #Then just return total
        return total