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


n=int(input())
q=Queue()#创建空队列
#把12345按顺序放入队列
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
while q.ask()%n!=0:#不能整除就循环
t=q.ask()
#确定每个数的个位，然后按照题目意思进行操作
    if t%10==1:
        q.enqueue(t*10+3)
        q.enqueue(t*10+5)
        q.dequeue()
    if t%10==2:
        q.enqueue(t*10+3)
        q.enqueue(t*10+4)
        q.dequeue()
    if t%10==3:
        q.enqueue(t*10+1)
        q.enqueue(t*10+4)
        q.dequeue()
    if t%10==4:
        q.enqueue(t*10+5)
        q.dequeue()