"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        room=[]
        intervals.sort(key=lambda x:x.start)
        for interval in intervals:
            if len(room)>0 and room[0]<=interval.start:
                heapq.heappop(room)  
            
            heapq.heappush(room,interval.end)
        return len(room)

        