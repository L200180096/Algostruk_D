import re

##Nomor 1
f = open('indonesia.txt', 'r', encoding='latin1')
teks = f.read()
f.close()
p = r'\s([Mm]e\w+)'
cocok = re.findall(p, teks)
