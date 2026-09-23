
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        if not intervals:
            return True

        res = [intervals[0]]

        for interval in intervals[1:]:
            start = interval.start
            end = interval.end

            prev_start = res[-1].start
            prev_end = res[-1].end

            if prev_end > start:
                return False
            else:
                res.append(interval)

        return True
