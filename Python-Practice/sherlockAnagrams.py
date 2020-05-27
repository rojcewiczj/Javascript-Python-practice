def sherlockAndAnagrams(s):
    dictionary  = {}
    count = 0
    inc = 1
    # for index, letter in enumerate(s):
    #     if letter not in dictionary:
    #         dictionary[letter] = [index]
    #     else:
    #         dictionary[letter].append(index)
    while inc < len(s):
        substring = s[0: inc]
        print(substring)
        if substring[::-1] in 