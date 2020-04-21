
import re

##Nomor 2


f=open('indonesia.txt', 'r', encoding='latin1')
teks= f.read()
f.close()

pola1= r'di\w+'

tampilan1=re.findall(pola1,teks)
print(tampilan1)

print('\n\n')

