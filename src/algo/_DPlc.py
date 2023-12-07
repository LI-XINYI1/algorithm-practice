import math

class Solution_279PerfectSquares:
    def numSquares(self, n: int) -> int:
      # 状态：dp[i] 完全平方和为i的最少数量
      # dp[i] = min(dp[i - j*j] + 1, dp[i])  i<=n, j^j<=i
      # preorder
      dp = [float('inf')]*(n+1)
      dp[0], dp[1] = 0,1
      for i in range(2,n+1):
         upper_j = int(pow(i,0.5))
         for j in range(1,upper_j+1):
            dp[i] = min(dp[i],dp[i-j*j]+1)
      return dp[n]

class Solution5___094_132:
    def minCut(self, s: str) -> int:
      # 状态：dp[i][j] 从i到j的字符串是否回文
      #     边界dp[i][i] = 1  目标dp[0][len-1]
      # dp[i][j] = dp[i+1][j-1] && s[i] == s[j]
      # i: larger to small    j: small to larger
      n = len(s)
      dp = [ [True]*n for _ in range(n)]
      for i in range(n-1, -1, -1):
         for j in range(i+1, n):
            dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
      rlt = [float("inf")] * n
      for i in range(n):
         if dp[0][i]:
               rlt[i] = 0
         else:
               for j in range(i):
                  if dp[j + 1][i]:
                     rlt[i] = min(rlt[i], rlt[j] + 1)
      return rlt[n-1]

      # 状态：dp[i]  从0到i的字符串都分割成回文的最小次数
      #     边界dp[0], dp[1] = 0,1  目标dp[len-1]
      # 递推公司：
      #   dp2[j] = min(dp2[j], dp2[i-1]+1)  
      #   prerequisite: s[i,j]回文
      # i: larger to small    j: small to larger      
      dp2 =[ [0]*n for _ in range(n)]
      dp2[0], dp2[1] = 0
      for j in range(1,n):
         for i in range(j+1):
            if dp2[i][j] == 0: #将s[i,j]分割的条件是s[i,j]为回文串
               continue        # 提前终止
            if i==0:    # 取得最小分割数，跳出循环
               dp2[j] = 0
               break 
            else:
               dp2[j] = min(dp2[j], dp2[i-1]+1)
      return dp2[n-1]

class Solution1359:
    def countOrders(self, n: int) -> int:
      # 状态：dp[i] 
      #     边界dp[1] = 1  目标dp[n]
      # 递推公司：
      #   dp[i] = dp[i-1]*C[2i][2] = dp[i-1]*i*(2i-1)
      #   在2i个位置里找两个位置放Pi, Di; 剩下2(i-1)个位置的排列=dp[i-1]
      # 先序
      rlt = 1
      MOD = 10**9 + 7
      for i in range(2, n+1):
         rlt = (rlt*(2*i-1)*i ) % MOD
      return rlt
    
class Solution1510:
    def winnerSquareGame(self, n: int) -> bool:
      squares = lambda x: (i * i for i in range(math.isqrt(x), 0, -1))
      dp = [False]*(n+1)
      for i in range(1, n+1):
         dp[i] =  not all(dp[i - s] for s in squares(i))
      return dp[-1]

class Solution70:
   def climbStairs(self, n: int) -> int:
      dp = [0]*(n+1)
      dp[0] = dp[1] = 1       
      # dp[2] = 2
      for i in range(2,n+1):
         dp[i] = dp[i-1] + dp[i-2]
      return dp[n]

class Solution746:
   def minCostClimbingStairs(self, cost: List[int]) -> int:
      dp = [0] * (len(cost)+1)          
      dp[0] = dp[1] = 0
      for i in range(2,len(dp)):
         dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
      return dp[i]
   
class Solution1137:
   def tribonacci(self, n: int) -> int:
      dp = [0]*4
      dp[0] = 0
      dp[1] = dp[2] = 1
      for i in range(3,n+1):
         dp[i%4] = dp[(i-1)%4] + dp[(i-2)%4] + dp[(i-3)%4]
      return dp[n%4]