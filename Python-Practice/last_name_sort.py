
last_names = ["John Locke",
  "Thomas Aquinas",
  "David Hume",
  "Rene Descartes"]

def sort_lastname(array):
    only_last = []
    for names in array:
        for characters in names:
            if characters == ' ':
                print(names.index(characters))
                only_last.append(names[names.index(characters) + 1: len(names)])
    print(only_last)
                 

sort_lastname(last_names)
