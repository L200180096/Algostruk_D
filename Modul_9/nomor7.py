##nomor7
class SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

    def __str__(self):
        return str(self.data)

a = SimpulPohonBiner('Ambarawa')
b = SimpulPohonBiner('Bantul')
c = SimpulPohonBiner('Cimahi')
d = SimpulPohonBiner('Denpasar')
e = SimpulPohonBiner('Enrekang')
f = SimpulPohonBiner('Flores')
g = SimpulPohonBiner('Garut')
h = SimpulPohonBiner('Halmahera Timur')
i = SimpulPohonBiner('Indramayu')
j = SimpulPohonBiner('Jakarta')

a.kiri = b; a.kanan = c
b.kiri = d; b.kanan = e
c.kiri = f; c.kanan = g
e.kiri = h;
g.kanan = i

def maxDepth(node):
    if node is None:
        return 0 ;
    else :
        kiri = maxDepth(node.kiri)
        kanan = maxDepth(node.kanan)
        if (kiri > kanan):
            return kiri+1
        else:
            return kanan+1

print('Tinggi maksimal dari Binary tree adalah', maxDepth(a))
