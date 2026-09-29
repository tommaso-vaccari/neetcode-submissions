class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        #UMPIRE : Understand Match Plan IMplement Review Evaluate
        # I need to return the minimum number of intervals that i have to remove
        # for obtaining a non overlapping list

        # I can use the approach usefull for intervals that is
        # sorting the list of intervals and couting how many of them i need to merge to make
        # them to not overlap
        if len(intervals) <= 1:
            return 0
        

        intervals = sorted(intervals, key = lambda x : x[0])
        print(intervals)

        result = list()
        result.append(intervals[0])
        to_remove = 0
        for start, end in intervals[1:]:
            if start < result[-1][1]:
                result[-1] = [result[-1][0], min(result[-1][1],end)]
                to_remove +=1
            else:
                result.append([start,end])
        print(result)
        return to_remove

        