def bracket_validator(input_string):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    
    
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in input_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
        
            last_open_bracket = stack.pop()
            if last_open_bracket != bracket_map[char]:
                return False

    return not stack 
