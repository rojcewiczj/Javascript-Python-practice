def longestPalindromicSubstring(string):
    i = 1 
	longest = ""
	if len(string) <= 1:
		return string[0]
	while(i < len(string)):
		if(string[i] == string[i -1]):
			left = i -1
			right = i
			while( left > 0 and right < len(string) -1 and string[left -1] == string[right + 1]):
				left -= 1
				right += 1
		    substring = string[left :right + 1]
			if(len(longest) < len(substring)):
				longest = substring
		if(i + 1 < len(string) and string[i + 1] == string[i-1]):
			left = i - 1
			right = i + 1
			while(left > 0 and right < len(string) -1 and string[left -1] == string[right + 1]):
				left -= 1
				right += 1
			substring = string[left : right + 1]
			if(len(longest) < len(substring)):
				longest = substring
		i += 1

    return longest