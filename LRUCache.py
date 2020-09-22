class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dicti = {}
        self.array = []

    def get(self, key: int) -> int:
        if key in self.array:
            self.array.remove(key)
            self.array.append(key)
            return self.dicti[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
      
        if key in self.array:
            self.array.remove(key)
            self.array.append(key)
            self.dicti[key] = value
        else:
            if len(self.array) < self.capacity:
                self.array.append(key)
                self.dicti[key] = value
            else:
                self.array.pop(0)
                self.array.append(key)
                self.dicti[key] = value
        