
import re

##Nomor 3


f=open('indonesia.txt', 'r', encoding='latin1')
teks= f.read()
f.close()

pola2= r'di \w+'

tampilan2=re.findall(pola2,teks)
print(tampilan2)

print('\n\n')

