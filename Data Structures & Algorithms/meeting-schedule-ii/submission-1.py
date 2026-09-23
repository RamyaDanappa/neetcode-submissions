
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        rooms = []

        for interval in intervals:
            start = interval.start
            end = interval.end

            # If the earliest available room is free,
            # reuse that room
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)

            # Put this meeting's end time into the heap
            heapq.heappush(rooms, end)

        return len(rooms)
