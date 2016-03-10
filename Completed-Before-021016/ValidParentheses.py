# Valid Parentheses
#http://www.codewars.com/kata/valid-parentheses/

def valid_parentheses(string):
    right = 0
    left = 0
    for letter in string:
        if letter == ")" and left <= right:
            return False
        elif letter == ")":
            right += 1
        elif letter == "(":
            left += 1
            
    if left == right:
        return True
    else:
        return False