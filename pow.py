class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        sum = 1
        former = 1
        if n > 0:
            for i in xrange(n):
                former = sum
                sum *= x
                if sum == former:
                    return sum
                elif abs(sum) == abs(former):
                    sum = sum if (n - i - 1) % 2 == 0 else former
                    return sum
        else:
            for i in xrange(0 - n):
                former = sum
                sum /= x
                if sum == former:
                    return sum
                elif abs(sum) == abs(former):
                    sum = sum if (n - i - 1) % 2 == 0 else former
                    return sum
        return sum
