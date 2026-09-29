class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # I need to merge overlapping intervals
        # Given [A,B] and [C,D] they overlap if
        # (C<=B) or (A<=D)
        # How to merge
        # If (C<=B) -> [A,D] 
        # if( A<= D) -> [C,B]
        
        # The algorithm
        # I can assume that i can start by comparing the first interval with the second
        # one, if they overlap i substitue the first one with the now overlapping and discard
        # the second, If they do no overlap i can go to the third

        
        # When i can tell if have finished to merge? when the legnth of the result has
        # not changed between merge rounds
        if len(intervals)<=1:
            return intervals
 

        intervals.sort(key=lambda x: x[0])
        result = list()
        result.append(intervals[0])
        for start, end in intervals:
            if start<= result[-1][1]:
                result[-1][1] = max(end,result[-1][1])
            else:
                result.append([start,end])

                    



        return result
                
            
            







