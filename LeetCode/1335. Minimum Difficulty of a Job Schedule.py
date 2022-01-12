class Solution:
    def minDifficulty(self, jobDifficulty, d):

        """

        """
        if not jobDifficulty or len(jobDifficulty) < d:
            return -1

        if len(jobDifficulty) == d:
            return sum(jobDifficulty)
        if d == 1:
            return max(jobDifficulty)

        """
        dp[i][j] finished jth job in ith day
        dp[i][j] = -1 if i > j
        dp[d][n]
           7  1  7  1  7  1

           0  1  2  3  4  5 

        0  7  7  7  7  7  7
        1 -1  8  14 8  14 8 
        2 -1 -1  15 15 15 15

        init
        dp[1][j] = max(jd[:j+1])
        dp[1][0] = jd[0]
        for j in range(1, n):
            dp[1][j] = max(dp[1][j-1], jd[j])
        dp[i][j] = dp[i-1][j-1] + jd[j]

        transfer
        dp[i][j]
        do k jobs in i-1 and k to j in ith max(jd[k+1:j+1])
        work = jd[j]
        for k in range(j-1, i)

        """
        n = len(jobDifficulty)
        # init
        dp = [[float('inf') for i in range(n)] for j in range(d)]

        dp[0][0] = jobDifficulty[0]
        for j in range(1, n-d+1):
            dp[0][j] = max(dp[0][j-1], jobDifficulty[j])

        for i in range(1, d):
            for j in range(i, n-(d-i)+1):
                # dp[i][j] = dp[i-1][j-1] + jobDifficulty[j]
                work = jobDifficulty[j]
                for k in range(j-1, i-2, -1):
                    dp[i][j] = min(dp[i-1][k]+work, dp[i][j])
                    work = max(work, jobDifficulty[k])
        # for i in range(1, d):
        #     for j in range(i, n-(d-i)+1):
        #         # k  0..k in i-1 k..j in i k~[i, j]





        self.dp = dp
        return dp[d-1][n-1]

        # process






if __name__ == '__main__':
    jobDifficulty = [11,111,22,222,33,333,44,444]
    # jobDifficulty = [7,  1,  7 , 1,  7,  1]
    d = 6
    s = Solution()
    k = s.minDifficulty(jobDifficulty, d)
    print(k)
