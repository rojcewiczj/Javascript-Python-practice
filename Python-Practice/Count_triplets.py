def countTriplets(arr, r):
    dicti = {}
    n = len(arr)
    for i in range(0, n):
        print("i :",i)
        for j in range(i+1, n):
            print("j :",j)
            for k in range(i+1, n):
                print("k :", k)
                if arr[k]/ arr[j] == r and arr[j] / arr[i] == r:
                    dicti[i + j + k] = [arr[i], arr[j], arr[k]]
    print(dicti)
