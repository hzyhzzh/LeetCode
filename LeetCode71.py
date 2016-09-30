class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result = []
        parsed_path = path.split('/')

        for pp in parsed_path:
            if pp == '.' or pp == '':
                continue
            elif pp == '..':
                if len(result) > 0:
                    result.pop()
            else:
                result.append(pp)

        return '/' + '/'.join(result)
