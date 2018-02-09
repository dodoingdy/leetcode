class Solution(object):
    def romanToInt(self, s):
        """
        :type s:str
        :rtypr:int
        """
        m1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n = m1[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if m1[s[i]] >= m1[s[i + 1]]:
                n += m1[s[i]]
            else:
                n -= m1[s[i]]
        return n
