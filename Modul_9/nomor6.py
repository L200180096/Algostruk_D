##nomor6
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

def size(node) :
    if node is None:
        return 0
    else:
        return (size(node.kiri)+1+ size(node.kanan))

print('Ukuran dari Binary tree adalah', size(a))
