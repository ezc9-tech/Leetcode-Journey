class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Instantiate our result list with all zeros
        res = [0] * len(temperatures)
        #Use a stack to keep track of temps and indexes
        stack = []

        #For every index and temp in temperatures
        for i, t in enumerate(temperatures):
            #If the stack exists and the current temp is greater than the last temp in the list
            while stack and t > stack[-1][0]:
                #Grab that temp and index
                stackT, stackInd = stack.pop()
                #Set the results index of the compared element to the first index of a greater element
                res[stackInd] = i - stackInd
            #Append the temp and index to the stack
            stack.append((t, i))
        #Return the result
        return res
        