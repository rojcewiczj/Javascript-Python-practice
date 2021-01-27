def valid(s):
    left = '('
    right = ')'
    count = 0
    for i in range(0, len(s)):
        if s[i] == '(':
            count += 1
        else:
            count -=1
            if(count < 0):
                print("false")
    if count != 0:
        print('false')
     
  
valid('()()(()((())(()((')

    
