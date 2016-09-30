#-*- coding:utf-8 -*-
class Solution(object):
    def decodeString(self, s):
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
        return s
