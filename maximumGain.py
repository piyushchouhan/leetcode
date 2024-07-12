def maximumGain(s,x,y):
        
        def maxScore1(s,x,y):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] + char == "ba":
                    stack.pop()
                    score += y
                else:
                    stack.append(char)

            newstack = []
            for char in stack:
                if newstack and newstack[-1] + char == "ab":
                    newstack.pop()
                    score += x
                else:
                    newstack.append(char)
            return score
        
        def maxScore2(s,x,y):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] + char == "ab":
                    stack.pop()
                    score += x
                else:
                    stack.append(char)

            print("".join(stack))
            newstack = []
            for char in stack:
                if newstack and newstack[-1] + char == "ba":
                    newstack.pop()
                    score += y
                else:
                    newstack.append(char)
            return score

        return max(maxScore1(s,x,y), maxScore2(s,x,y))

s = "aabbaaxybbaabb"
x = 5
y = 4
print(maximumGain(s, x, y)) 