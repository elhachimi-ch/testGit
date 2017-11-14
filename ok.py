import re
import math
import sys
import lib
import re
from functools import reduce as r

sys.stdin= open("f.txt", "r+")
T= int(input())
for i in range(T):
    s= input().split(" ")
    l= int(s[0])
    c= int(s[1])
    kharita= []
    for i in range(l):
        kharita.append(input())
    print(kharita)
    for i in range(l):
        for j in range(c):
            if kharita[i][j] == 'x':
                nbr+=1
                co= [i+1, j+1]
	print("OK")
