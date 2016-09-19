"""
Input:
["a","b","c","d","e"]
1
Output:
["","a","b","c","d","e"]
Expected:
["a","b","c","d","e"]
"""
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        length = 0
        start = 0
        for i in range(len(words)):
            length = len(words[i]) +length
            if(length + i - start >= maxWidth and start != len(words) - 1 ):
                    sub_len = 0
                    for j in range(start, i):
                        sub_len += len(words[j])
                    if(i- start -1 >0):
                        seprate =  (maxWidth - sub_len + i - start - 2 ) / (i - start - 1 ) ##UP(A/B) = A+B-1 /B
                    else:
                        seprate = maxWidth - sub_len
                    element = ""
                    for j in range(start, i-1):
                        if(sub_len + seprate * (i - j) > maxWidth and  j == i-2 and seprate >= 1):
                            element += words[j] + ' '*(seprate-1)
                        else:
                            element += words[j] + ' '*seprate
                    if(i-1 >= 0):
                        element += words[i-1]
                    start = i
                    length = 0
                    result.append(element)


            if(start == len(words) - 1 ):
                    element = words[start] + ' '*(maxWidth - len(words[start]))
                    result.append(element)
        return result

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return []

        justifiedLines = []
        firstWordIdx = 0
        lineLen = len(words[0])
        for i in xrange(1, len(words)):
            if lineLen + 1 + len(words[i]) <= maxWidth:
                lineLen += (1 + len(words[i]))
            else:
                line = self.generateEvenSpacedLine(firstWordIdx, i - 1, maxWidth, words, lineLen)
                justifiedLines.append(line)
                firstWordIdx = i
                lineLen = len(words[i])

        lastLine = self.generateLeftJustifiedLine(firstWordIdx, len(words) - 1, maxWidth, words, lineLen)
        justifiedLines.append(lastLine)
        return justifiedLines

    def generateEvenSpacedLine(self, firstWordIdx, lastWordIdx, maxWidth, words, lineLen):
        numWords = lastWordIdx - firstWordIdx + 1
        if numWords == 1:
            return words[firstWordIdx] + ' '*(maxWidth - lineLen)

        numGaps = numWords - 1
        spaceToDistr = maxWidth - lineLen
        gapSpace, extraGaps = divmod(spaceToDistr, numGaps)
        line = words[firstWordIdx]

        for i in xrange(firstWordIdx + 1, lastWordIdx + 1):
            line += (' '*(gapSpace + 1))
            if extraGaps > 0:
                line += ' '
                extraGaps -= 1

            line += words[i]

        return line

    def generateLeftJustifiedLine(self, firstWordIdx, lastWordIdx, maxWidth, words, lineLen):
        line = words[firstWordIdx]
        for i in xrange(firstWordIdx + 1, lastWordIdx + 1):
            line += (' ' + words[i])
        line += (' '*(maxWidth - len(line)))
        return line
