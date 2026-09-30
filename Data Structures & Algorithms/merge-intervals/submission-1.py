class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # I need to merge intervals, to avoid bookeping overhead and having to 
        # do O(n^2) checks I can instead sort the intervals array by the starting point.
        # The invariant is that at any step i the result array contains intervals
        # that are disjointed and that span the first i full intervals. 
        # This invariant gurantess me that i have to check overlapping only with the last
        # interval

        if len(intervals)<=1:
            return intervals

        intervals.sort(key = lambda x : x[0])
        result = list()
        result.append(intervals[0])

        for start, end in intervals[1:]:
            # I have to compare only with the last interval
            if start <= result[-1][1]:
                #They do overlap, i keep the merge of the two
                result[-1][1] = max(result[-1][1], end)
            else:
                #They do not overlap, i can add the the disjointed interval
                result.append([start,end])


        return result 
            





        