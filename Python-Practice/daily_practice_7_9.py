# to_ignore = ["ew"]
# string = "eeeeeee"

# all_ignore = True

# for character in string:
#     if character not in to_ignore:
#         all_ignore = False

# if all_ignore == True:
#     print({})
# else:
#     print(string)

def is_true(s):
    
    array = []
    rev_array = []

    for letter in s:
        array.append(letter)
        try:
            int(letter)
        except:
            print("nope")

    for letter in reversed(array):
        rev_array.append(letter)

    if array != rev_array:
        print("nope")
    
    if len(array) % 2 != 0:
        if array[len(array) // 2] != "0":
            print("nope")

    print(array)


is_true("12034")