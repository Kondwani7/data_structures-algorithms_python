#interval class
from tracemalloc import start


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    find if a student can attend all meetings (no overlapping intervals)
    return True if no overlap, otherwise false (overlap)
    """
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda i : i.start)

        for i in range(1, len(intervals)):
            #first interval
            i1 = intervals[i -1 ]
            #second interval to compared
            i2 = intervals[i]
            #overlapp
            if i1.end > i2.start:
                return False
        return True