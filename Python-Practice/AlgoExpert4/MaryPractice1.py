

number = 1
string = "hello"

array = []
dictionary = {}

# function addToArray(){
#     for(var i = 0; i < 100; i++){
#         console.log(i)
#     }
# }

def addToArray(): 
    number = 1
    dicti = {}
    word = "hello"
    while len(word) > 0:
        # defining an empty array at the beginning of the loop
        arr = []
        # creating an iterator to loop from 0 to the len of the string (word)
        for i in range(0, len(word)):
            # appending to our empty array the letter of the string(word) at the index of i
            arr.append(word[i])
        
        dicti[number] = arr
        number += 1
        # every loop, the word gets shorter by 1, 0 is the start, the colon (:) means up to, and len(word) -1 means you incude every letter up to
        # the end of the word - the last letter.
        word = word[0:len(word)- 1]

      
    print(dicti)
        
        

  
print(addToArray())





