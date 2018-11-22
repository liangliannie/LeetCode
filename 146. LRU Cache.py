from collections import deque
import collections
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cnt = collections.defaultdict(int)
        self.cache = {}
        self.visited = collections.deque()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.visited.append(key)
            self.cnt[key] += 1
            return self.cache[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.cache and len(self.cache) >= self.cap:
            while self.visited:
                k = self.visited.popleft()
                self.cnt[k] -= 1
                if self.cnt[k] <= 0:
                    del self.cache[k]
                    break
        self.cache[key] = value
        self.visited.append(key)
        self.cnt[key] += 1
        return
    
class LRUCache1(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.q = deque()
        self.d = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d: 
            return -1
        self.q.remove(key)
        self.q.append(key)
        return self.d[key] 

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key in self.q:
            self.q.remove(key)
            self.q.append(key)
            self.d[key]=value
        else:
            if len(self.q)==self.c:
                ql = self.q.popleft()
                del self.d[ql]

            self.q.append(key)
            self.d[key]=value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)