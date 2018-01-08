# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key = operator.attrgetter('start'))
        result = [intervals[0]]
        for n in intervals[1:]:
            gg = result.pop()
            if gg.end < n.start:
                result.append(gg)
                result.append(n)
            else:
                result.append(Interval(min(gg.start, n.start), max(gg.end, n.end)))            return result
