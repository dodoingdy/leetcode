class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        key = 1
        i = length - 1
        while key != 0:
            val = digits[i] + 1
            key = val / 10
            digits[i] = val % 10
            i -= 1
            if i < 0:
                digits.insert(0, key)
                break
        if digits[0] == 0:
            del digits[0]
        return digits
