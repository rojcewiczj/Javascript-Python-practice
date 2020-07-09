to_ignore = ["ew"]
string = "eeeeeee"

all_ignore = True

for character in string:
    if character not in to_ignore:
        all_ignore = False

if all_ignore == True:
    print({})
else:
    print(string)