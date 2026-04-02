class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #For this question since the array is sorted we can use a 
        #left and right pointer
        l = 0
        r = len(numbers) - 1

        #Once both pointers reach each other we can stop
        while l <= r:
            #Find what remains of the target once we subtract the sum
            #of where r and l are
            remaining = target - (numbers[r] + numbers[l])
            #If what remains is positive then we need to move l up
            #until what remains is zero
            if remaining > 0:
                l += 1
            #Else we subtract are down until what remains is zero
            elif remaining < 0:
                r -= 1
            #Once we reach zero then return the array of indexes
            #making sure to add one to each as the instructions say
            else:
                return [l + 1, r + 1]

