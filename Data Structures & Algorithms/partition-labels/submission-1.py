from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
                # This problem was meant to be approached as overlapping intervals

        app = defaultdict(int)

        for i, c in enumerate(s):
            app[c] = i
        

        size,end = 0,0
        res = list()
        for i, c in enumerate(s):
            size+=1
            if end < app[c]:
                end = app[c]
            
            if i == end:
                res.append(size)
                size = 0
        return res