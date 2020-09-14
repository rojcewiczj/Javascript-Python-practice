arrays = [[1,5],[2,3],[1,6],[3,5]]


def add(num, total):
    total = total +  num
    return total

def subtract(num, total):
    total = total - num
    return total


operations = {
    1 : add,
    2 : subtract

}



for arr in arrays:
    operations[arr[0]](arr[1], total)

print(total)
