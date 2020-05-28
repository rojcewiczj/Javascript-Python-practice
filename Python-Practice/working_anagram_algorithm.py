def sherlockAndAnagrams(s):
    count = 0
    res = [s[i: j] for i in range(len(s)) 
          for j in range(i + 1, len(s) + 1)] 
    substrings = []
    for substring in res:
        substrings.append(''.join(sorted(substring)))
    dictionary = {}
    for substring in substrings:
        if substring not in dictionary:
            dictionary[substring] = 1
        else:
            dictionary[substring] += 1
            for num in range(1, dictionary[substring]):
                count += 1

        
    return count