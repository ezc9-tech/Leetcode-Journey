class Solution:
    def minOperations(self, logs: List[str]) -> int:
        #Have a stack to keep track of how deep we are in the folder structure
        stack = []

        #For each log in logs
        for log in logs:
            #If we go back into a parent folder then remove a log from the stack
            if log == "../":
                #Make sure that the stack exists
                if stack:
                    stack.pop()
            #If you remain in the same folder then don't do anything
            elif log == "./":
                pass
            #Else add on the log into the stack
            else:
                stack.append(log)
        #The length of the stack should be the amount of operations so return it
        return len(stack)