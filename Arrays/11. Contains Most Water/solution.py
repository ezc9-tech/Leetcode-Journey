class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Look at both ends of the array
        l, r = 0, len(heights) - 1
        #Keep track of the max area
        maxArea = 0

        #You can stop once l and r are the same
        while l < r:
            #Calculate the area using the min of the left and right height and the distance between them
            area = (r - l) * min(heights[l], heights[r])
            #Change the area if it is larger
            maxArea = max(area, maxArea)
            #If the left height is smaller then move it up
            if heights[l] < heights[r]:
                l += 1
            #Else move the right height back
            else:
                r -= 1
        #Retur the max area
        return maxArea