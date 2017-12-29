class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]
        result = [0] * (max(len(a), len(b)) + 1)
        for i in range(min(len(a), len(b))):
            result[i] = int(a[i]) + int(b[i])
        if len(a) < len(b):
            for i in range(len(a), len(b)):
                result[i] = int(b[i])
        else:
            for i in range(len(b), len(a)):
                result[i] = int(a[i])
        for i, n in enumerate(result):
            if i == len(result) - 1:
                break
            result[i] = n % 2
            result[i + 1] += n / 2
        if result[len(result) - 1] == 0:
            result = result[:-1]
        end = ''
        for i, n in enumerate(result):
            end += str(n)
        return end[::-1]
