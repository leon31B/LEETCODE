class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        currRow = 0
        goingDown = False

        for c in s:
            rows[currRow] += c

            if currRow == 0 or currRow == numRows - 1:
                goingDown = not goingDown

            if goingDown:
                currRow += 1
            else:
                currRow -= 1

        return "".join(rows)