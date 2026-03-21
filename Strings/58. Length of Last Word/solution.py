class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #So first we need to clean up the string
        s = s.strip()
        #Then we need to split the string into a list
        words = s.split(" ")
        #Then return the length of the last word
        return len(words[-1])