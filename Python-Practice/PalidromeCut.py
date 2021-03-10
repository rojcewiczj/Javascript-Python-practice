s = "jkjabacodoc"

def cut(s):
    has_pal = True
    while has_pal == True:
        i = 1
        stringLength = len(s)
        longest = ""
        while(i < len(s)):
            if(s[i-1] == s[i]):
                left = i - 1
                right = i
                while(left > 0 and right < (len(s)- 1) and s[left -1] == s[right + 1]):
                    left -= 1
                    right += 1
                if(((right + 1) - left) > len(longest)):
                    longest = s[left: (right +1)]
            if(i < (len(s) -1) and s[i-1] == s[i + 1]):
                left = i - 1
                right = i + 1
                while(left > 0 and right < (len(s)- 1) and s[left -1] == s[right + 1]):
                    left -= 1
                    right += 1
                if(((right + 1) - left) > len(longest)):
                    longest = s[left: (right +1)]
            i += 1 
            
        s = s.replace(longest, "")
        if len(s) == stringLength:
            has_pal = False
    return s

print(cut(s))
                
