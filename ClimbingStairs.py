class Solution:
    def climbStairs(self, n: int) -> int:
        back_back,back = 0,1
        for _ in range(n):
            back_back,back = back,back_back + 1
        return back