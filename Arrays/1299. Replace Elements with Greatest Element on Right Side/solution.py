class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #Grab the number of numbers in the array
        n = len(arr)
        #Create a pre-allocated list for each number
        ans = [0] * n
        #Create a variable for the right max
        rightMax = -1

        #Look at every index of the array backwords
        for i in range(n-1, -1 , -1):
            #Set the answer array index equal to the rightMax
            ans[i] = rightMax
            #Set rightMax equal to the greatest between it and the index of the arr
            rightMax = max(arr[i], rightMax)
        
        #Return the answer
        return ans