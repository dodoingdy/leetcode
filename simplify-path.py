class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return ''
        result = ['']
        a = path.split('/')
        for i in a:
            if not i:
                continue
            else:
                if result:
                    tmp = result.pop()
                else:
                    if i == '..' or i == '.':
                        continue
                    else:
                        result.append(i)
                        continue
                if i == '..':
                    continue
                elif i == '.':
                    result.append(tmp)
                else:
                    result.append(tmp)
                    result.append(i)
        end = '/'.join(result)
        if not end:
            end += '/'
        elif end[0] != '/':
            end = '/' + end
        return end
