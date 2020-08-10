
def get_max_sum(array, target):
    window_sum = 0
    k = target
    sub_arrays = []

    for i in range(0, k):
        for i in range(0,k):
            window_sum += array[i]
        if window_sum == target:
            sub_arrays.append(k)
      
        for i in range(k, len(array)):
            window_sum += array[i] - array[i - k]
            if window_sum == target:
                sub_arrays.append(k)
        window_sum = 0
        k -= 1
  
    sub_arrays.sort()
    return sub_arrays[0] + sub_arrays[1]
    

print(get_max_sum([1,4,5,1,1,1,1,1,3,2], 5))


class example:
    def __init__(self):
        self.name = "example"

ex = example()
print(ex)
  