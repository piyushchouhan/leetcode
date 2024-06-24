def myAtoi(s: str) -> int:
    # Step 1: Ignore leading whitespace
    s = s.lstrip()

    if not s:
        return 0

    # Step 2: Check for sign
    sign = 1
    index = 0
    if s[0] == '-':
        sign = -1
        index = 1
    elif s[0] == '+':
        index = 1

    # Step 3: Read digits and form the number
    result = 0
    while index < len(s) and s[index].isdigit():
        result = result * 10 + int(s[index])
        index += 1

    # Apply sign
    result *= sign

    # Step 4: Handle out of range values
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX

    return result

# Test cases
print(myAtoi("  -042"))      # Output: -42
print(myAtoi("42"))          # Output: 42
print(myAtoi("   +12345"))   # Output: 12345
print(myAtoi("   -123abc"))  # Output: -123
print(myAtoi("abc123"))      # Output: 0
print(myAtoi(""))            # Output: 0
print(myAtoi("2147483648"))  # Output: 2147483647
print(myAtoi("-2147483649")) # Output: -2147483648
