  
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
  
string = "aab"
string_to_match = "c*a*bbbe*f"
  
def isMatch(s, p):
    inc = 0
    Match = {}
    while inc < len(string_to_match):
        if string_to_match[inc] in string:
            Match[string_to_match[inc]] = True
        elif string_to_match[inc] == "*":
            Match[string_to_match[inc - 1]] = True
        else:
            Match[string_to_match[inc]] = False

        inc += 1
    print(Match)






isMatch(string, string_to_match)
        