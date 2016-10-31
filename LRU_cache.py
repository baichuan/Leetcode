class LRUCache(object):

    def __init__(self, capacity):

        self.dict = collections.OrderedDict()
        self.remain = capacity


    def get(self, key):

        if key not in self.dict:
            return -1

        v = self.dict.pop(key) 
        self.dict[key] = v   # set key as the newest one

        return self.dict[key];


    def set(self, key, value):

        if key in self.dict:    
            self.dict.pop(key)

        else:
            if self.remain > 0:
                self.remain -= 1 
               
            else:  # self.dic is full
                self.dict.popitem(last=False) 

        self.dict[key] = value 
