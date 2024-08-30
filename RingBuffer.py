class RingBuffer:
    def __init__(self, size):
        self.size_array_data=size
        self.arrayData = [None] * size
        self.p_read=0
        self.p_write=0
        self.count=0

    def get_size_ring_buffer(self):
        return self.size_array_data

    def set(self, frame):
        self.arrayData[self.p_write]=frame
        self.p_write=(self.p_write+1)%self.get_size_ring_buffer()
        if self.count == self.get_size_ring_buffer():
            self.p_read = (self.p_read+1)%self.get_size_ring_buffer()
        else:
            self.count+=1

    def get(self):
        if self.count==0:
            return None

        frame = self.arrayData[self.p_read]
        self.arrayData[self.p_read]=None
        self.p_read = (self.p_read+1)%self.get_size_ring_buffer()
        self.count-=1
        return frame
