# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 12:43 2020

@author: Rupa-421
"""


import urllib.request
r=input()
w=r.lower()
#-->City name is stored.

p=urllib.request.urlopen("https://www.swiggy.com/")
#-->A file of source code of swiggy website is stored in p.
g=p.read()
#-->The file is opened in g
l=g.decode()
#-->It decodes the byte file into string format.
k=l.split(":")
if w==("bangaluru" or "bengalore"):
    w="bangalore"
elif w=="calcutta":
    w="kolkata"
elif w=="bombay":
    w="mumbai"
try:
    x=k.index('"'+w+'","cityId"')
    g=k[x+2]
    if "true" in g:
         print("YES😋"+"."+"U can enjoy the swiggy online delivery in "+w+".")
except:
       print("NO😞.Sorry,hope may swiggy extend to your city in future.")
print()
g="'STAY HOME SAVE LIVES 😷'"
print(g.center(35))


