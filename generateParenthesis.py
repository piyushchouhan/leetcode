def generateParenthesis(n):
    def backtrack(S, left, right):
        if len(S) == 2 * n:
            result.append(S)
            return
        if left < n:
            backtrack(S + '(', left + 1, right)
        if right < left:
            backtrack(S + ')', left, right + 1)

    result = []
    backtrack('', 0, 0)
    return result

n = 4
print(generateParenthesis(n))

