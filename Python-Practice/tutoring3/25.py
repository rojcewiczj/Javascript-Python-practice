
a = "egg"
b = "add"
def check(a , b):
    dictionary_a = {}
    dictionary_b = {}
    if len(a) != len(b):
        return False

    for i in range(0, len(a)):
        if a[i] not in dictionary_a:
            dictionary_a[a[i]] = [i] 
        else:
            dictionary_a[a[i]].append(i)
        if b[i] not in dictionary_b:
            dictionary_b[b[i]] = [i] 
        else:
            dictionary_b[b[i]].append(i)
            
        if dictionary_a[a[i]] != dictionary_b[b[i]]:
            return False
    return True

print(check(a,b))
        

   
        