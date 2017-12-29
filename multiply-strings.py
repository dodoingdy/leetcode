class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        results = [0] * 230
        for i, m in enumerate(num1):
            for j, n in enumerate(num2):
                results[i + j] += int(m) * int(n)
        for i, n in enumerate(results):
            temp = n / 10
            if i >= len(results) - 1:
                break
            results[i] = n % 10
            results[i + 1] += temp
        for i in range(len(results) - 1, -1, -1):
            if i == 0:
                break
            if results[i] == 0:
                results = results[:-1]
            else:
                break
        end = ''
        for i in results:
            end += str(i)
        end = end[::-1]
        return end
