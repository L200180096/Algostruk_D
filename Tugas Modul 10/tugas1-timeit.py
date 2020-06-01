# 1).
from timeit import timeit
import random

# A. jml cara 1
def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(1, n+1):
        hasilnya += i
    return hasilnya

# B. jml cara 2
def jumlahkan_cara_2(n):
    return (n*(n+1))/2

# C. Insertion Sort
def insertionsort(a):
    for i in range(1, len(a)):
        nilai = a[i]
        b = i
        while b > 0 and nilai < a[b - 1]:
            a[b] = a[b-1]
            b -= 1
        a[b] = nilai


x = 1000
y = [3, 4, 2, 1, 2, 5, 9, 3]

def jml1():
    jumlahkan_cara_1(x)
def jml2():
    jumlahkan_cara_2(x)
def inst():
    insertionsort(y)

if __name__ == '__main__':
    import timeit
    print("====================jumlahkan cara 1 timeit")
    print(timeit.timeit("jml1()", setup="from __main__ import jml1"))
    print("====================jumlahkan cara 2 timeit")
    print(timeit.timeit("jml2()", setup="from __main__ import jml2"))
    print("====================insertionSort timeit")
    print(timeit.timeit("inst()", setup="from __main__ import inst"))
