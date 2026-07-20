class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(n_open, n_close):
            if n_open == n_close == n:
                res.append(''.join(stack))
                return
            
            if n_open < n:
                stack.append('(')
                dfs(n_open + 1, n_close)
                stack.pop()

            if n_close < n_open:
                stack.append(')')
                dfs(n_open, n_close + 1)
                stack.pop()

        dfs(0, 0)
        return res