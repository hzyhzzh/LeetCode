# -*- coding:utf-8 -*-
"""
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        self.n = n
        self.ans = []
        self.upperlime = (1 << n) - 1
        self.test(0, 0, 0);
        return self.result

    def test(self, row, ld, rd):
        """
        row代表每一列的禁放位
        ld代表左上到右下的 斜向上对角线 禁放位
        rd代表右上到左下的 斜向下对角线 禁放位
        """
        if row != self.upperlime :
            pos = self.upperlime & (~(row | ld | rd ) )
            while( pos) :
                p = pos & (~pos +1 ) ##get the most right bit
                pos = pos - p
                self.test(row | p, (ld | p ) <<1 ,(rd | p ) >>1)
                for i in range(0, self.n):
                    if p & 1<<i :
                        element = "."*i  + 'Q' + "."*(self.n - i-1)
                        if(element not in self.ans):
                            self.ans.append(element)
                        break


        else:
            self.result.append(self.ans)
            self.ans = []
