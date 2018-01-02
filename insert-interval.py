# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        starts = {}
        ends = {}
        l = []
        for i in intervals:
            if i.start not in starts:
                starts[i.start] = 1
            else:
                starts[i.start] += 1
            ends[i.end] = 1
            l.append(i.start)
            l.append(i.end)
        if newInterval.start not in starts:
            starts[newInterval.start] = 1
        else:
            starts[newInterval.start] += 1
        ends[newInterval.end] = 1
        l.append(newInterval.start)
        l.append(newInterval.end)
        l.sort()
        r = []
        results = []
        for i in l:
            if i in starts and starts[i]:
                print 'true ', i
                r.append(i)
                starts[i] -= 1
            else:
                print r
                b = r.pop()
                print 'false ', b
                if not r:
                    results.append([b,i])
        return results
