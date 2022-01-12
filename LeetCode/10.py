class Solution:
    def match(self, s, p):

        if not p:
            return not s

        if not s and len(p) == 1:
            return False

        nrows = len(s) + 1
        ncols = len(p) + 1

        dp = [[False] * ncols for i in range(nrows)]

        dp[0][0] = True

        for i in range(2, ncols):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]

        """
        1. s[i] == p[j] or p[j] == '.'
        row = i+1
        col = j+1
        dp[row][col] = dp[row-1][col-1]
        
        2. p[j] == '*'
            2.1 p[j-1] = s[i] or p[j-1] == '.'
                dp[row][col] = dp[r-1][c] 
            2.2 p[j-1] != s[i] and p[j-1] == '.'
                dp[row][col] = dp[r][c-2]
            2.3 p[j-1] != s[i]
                dp[row][col] = dp[r][c-2]
            
        """

        for row in range(1, nrows):
            i = row - 1
            for col in range(1, ncols):

                j = col - 1
                # case 1
                if s[i] == p[j] or p[j] == '.':
                    dp[row][col] = dp[row-1][col-1]
                elif p[j] == '*':
                    if p[j-1] == s[i] or p[j-1] == '.':
                        dp[row][col] = dp[row-1][col] or dp[row][col-2]
                    else:
                        dp[row][col] = dp[row][col-2]
                else:
                    dp[row][col] = False

        return dp[-1][-1]

