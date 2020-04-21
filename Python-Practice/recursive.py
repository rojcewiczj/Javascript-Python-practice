def recursive_counter(count):
    if count == 0:
        return
    print(count)
    recursive_counter(count - 1)


recursive_counter(5)