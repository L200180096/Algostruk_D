import re

##Nomor 1


f=open('indonesia.txt', 'r', encoding='latin1')
teks= f.read()
f.close()

pola= r'me\w+'

tampilan=re.findall(pola,teks)
print(tampilan)

print('\n\n')
