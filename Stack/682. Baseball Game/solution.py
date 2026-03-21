class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #We need a stack to keep track of the scores
        scores = []
        
        #For every operation
        for oper in operations:
            #If it is a + then remove two scores from the stack and add them
            #Then add the result of the sum of the two to the stack
            if oper == "+":
                scores.append(scores[-1] + scores[-2])
            #If it is a C then remove the score from the stack
            elif oper == "C":
                scores.pop()
            #If it is a D then double the last score and append them to the stack
            elif oper == "D":
                scores.append(scores[-1] * 2)
            #Else add an int conversion of the oper to the stack
            else:
                scores.append(int(oper))
        #Return the sum of all the scores to get the total and return it
        return sum(scores)
            
        