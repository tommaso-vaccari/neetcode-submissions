class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #UMPIRE 
        # The main idea that i have is that i need to find the correct insertion point
        # for the interval that is guranteed to be unique given the nature for the problem.
        # For istance immagine that i have s3,e3 to insert and i have s1,e1 e s2, e2
        # for how it's organized initially i am sure abouth the fact that s2>e1 and so i need
        # to decide where to place my new interval, for istance just before the interval 
        # that has the same start or a greater start and then run the linear algorithm to merge
        # them

        

        temp = list()
        i = 0
        while i < len(intervals):
            if newInterval[0]<=intervals[i][0]:
                #I have found where i need to place my interval, i need to place it in position
                # i and move to one position right all the others
                break
            temp.append(intervals[i])
            i+=1
        
        # Now i have to look where i have to insert the new interval
        #If I it's one i append the new interval and then i append the entire array 
        result = list()
        temp = intervals[:i] + [newInterval] + intervals[i:]
        
        # Now i can run the merge algorithm maintaining the property of checking just the last one
        result.append(temp[0])
        
        for interval in temp[1:]:
            
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                #they do not overlap, i can just append it to result
                result.append(interval)
        return result
            





        