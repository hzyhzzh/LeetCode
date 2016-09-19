
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.Ans =0
        self.n = n
        self.upperlime = (1 << n) - 1
        self.test(0, 0, 0);
        return self.Ans

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


        else:
            self.Ans +=1
