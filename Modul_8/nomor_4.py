import heapq
class PriorityQueue(object):
    def __init__(self):
        self.qlist = []
    def __len__(self):
        return len(self.qlist)
    def isEmpty(self):
        return len(self) == 0
    def enqueue(self,data,priority):
        heapq.heappush(self.qlist, (priority,data))
        self.qlist.sort()
    def dequeue(self):
        return self.qlist.pop(-1)
    def getFrontMost(self):
        return self.qlist[-1]
    def getRearMost(self):
        return self.qlist[0]
    
a = PriorityQueue()
a.enqueue("Irfananda", 5)
a.enqueue("Irsyad", 2)
a.enqueue("Ainun", 11)
a.enqueue("Nauval", 6)
print("ProrityQueue Front==>",a.getFrontMost())
print("PriorityQueue Rear",a.getRearMost())


class Queue():
    def __init__(self):
        self.qlist=[]
    def isEmpty(self):
        return len(self)==0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self,data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.isEmpty(),"Antria sedang kosong"
        return self.qlist.pop(0)
    def getFrontMost(self):
        return self.qlist[0]
    def getRearMost(self):
        return self.qlist[len(self.qlist)-1]


q = Queue()
q.enqueue(7)
q.enqueue(11)
q.enqueue(12)
q.enqueue(18)
print("queue front==>",q.getFrontMost())
print("queue rear==>",q.getRearMost())
