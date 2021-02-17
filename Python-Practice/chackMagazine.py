




str_1 = "hello"
str_2 = "helilo"

def check():
    for i in range(0, len(str_2)):
        if i == len(str_2) -1:
            return str_2[i]

        if str_1[i] != str_2[i]:
            return str_2[i]

print(check())


