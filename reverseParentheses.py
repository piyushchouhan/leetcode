def reverseParentheses(s: str) -> str:
    stack = []
    for char in s:
        if char == ')':
            temp = []
            # Pop characters until '(' is found
            while stack and stack[-1] != '(':
                temp.append(stack.pop())
            # Remove the '('
            stack.pop()
            # Push the reversed substring back onto the stack
            stack.extend(temp)
        else:
            stack.append(char)
    
    # Join the characters to form the resulting string
    return ''.join(stack)

# Example usage:
s = "(u(love)i)"
print(reverseParentheses(s))  # Output: "iloveu"
