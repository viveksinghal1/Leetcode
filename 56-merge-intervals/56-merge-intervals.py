class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        
        index = 0
        
        intervals.sort(key= lambda x: x[0])
        
        res.append(intervals[0])
        
        intervalsLength = len(intervals)
        
        for i in range(1, intervalsLength):
            
            if (intervals[i][0] <= res[index][1]):
                if intervals[i][1] > res[index][1]:
                    res[index][1] = intervals[i][1]
                    
            else:
                res.append(intervals[i])
                index += 1
        
        return res