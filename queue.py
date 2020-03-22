class Queue:#先定义队列
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    
    def ask(self):
        return self.items[0]#这里只是取队列中的队首，不改变队列
    
    def get_items(self):
        return self.items