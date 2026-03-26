class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #Assume in the worst case no students can eat sandwiches
        res = len(students)
        #Get a hashmap of the preferences for the students
        hashmap = Counter(students)

        #For every sandwhich
        for s in sandwiches:
            #If there is a student with that preference in the hashmap
            if hashmap[s] > 0:
                #Take that student out of the hashmap
                hashmap[s] -= 1
                #Lower our result
                res -= 1
            #If are no students with that preference then that means we have some students left over so return them
            else:
                return res
        #Else you can return the res which should be zero
        return res
