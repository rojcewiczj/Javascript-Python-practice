def find_triplets(arr, total):
    array=[]
    for first_element in arr:
        for check in arr:
            for second_check in arr:
                if first_element + check + second_check == total:
                    array.append([first_element, check, second_check])
    print(array)
        
  

find_triplets([12,23,-5,-12,-8,4,7,3,10], 11)