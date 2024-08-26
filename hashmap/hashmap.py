class HashMap:
    def __init__(self):
        self._initial_capacity = 7  # Initial bucket capacity
        self._buckets = [[] for _ in range(self._initial_capacity)]
        self._size = 0  # Number of key-value pairs
    
    def _hash(self, key):
        r, c = key  # Assuming the key is a tuple (row, column)
        return (r * 31 + c) % len(self._buckets)  # Custom hash function

    def _rehash(self):
        # Double capacity and rehash all entries
        new_capacity = (len(self._buckets) * 2) - 1  # Ensure odd capacity
        new_buckets = [[] for _ in range(new_capacity)]
        
        # Rehash all current entries
        for bucket in self._buckets:
            for k, v in bucket:
                new_index = (k[0] * 31 + k[1]) % new_capacity
                new_buckets[new_index].append((k, v))
        
        self._buckets = new_buckets  # Replace with new buckets
    
    def set(self, key, value):
        idx = self._hash(key)
        bucket = self._buckets[idx]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # If the key exists, update its value
                bucket[i] = (key, value)
                return
        
        # If the key doesn't exist, add it
        bucket.append((key, value))
        self._size += 1
        
        # Check load factor and rehash if necessary
        if (self._size / len(self._buckets)) >= 0.8:
            self._rehash()
    
    def get(self, key):
        idx = self._hash(key)
        bucket = self._buckets[idx]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError("Key not found in HashMap.")
    
    def remove(self, key):
        idx = self._hash(key)
        bucket = self._buckets[idx]
        
        # Iterate to find the key and remove it
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return
    
    def clear(self):
        self._buckets = [[] for _ in range(self._initial_capacity)]
        self._size = 0
    
    def capacity(self):
        return len(self._buckets)
    
    def size(self):
        return self._size
    
    

    def keys(self):
        keys_list = []
        for bucket in self._buckets:
            for k, v in bucket:
                keys_list.append(k)
        return keys_list
