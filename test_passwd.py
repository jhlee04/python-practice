#!/usr/bin/env python
from pprint import pprint 
import re 
infile = open("/etc/passwd", 'r') 
lines =  infile.readlines()
passwd = { }  #  declare empty dictionary
dir_name = [] ; dir = [] 
for line  in lines:
    item=line.split(":")
    if int(item[2]) > 500 :
        dir.append(item[5]) 
        name =  item[5].split("/") 
        del name [-1]
        dir_name.append("/".join(name))
        dir_name=list(set(dir_name))
p=re.compile('[/]\w+')

for n in dir_name : 
    passwd[n] = []  
for name in dir : 
     if p.match(name).group() == dir_name[0]:
         passwd[dir_name[0]].append(p.findall(name)[-1])
     elif p.match(name).group() == dir_name[1]:
         passwd[dir_name[1]].append(p.findall(name)[-1])
     elif p.match(name).group() == dir_name[2]:
         passwd[dir_name[4]].append(p.findall(name)[-1])
del passwd[dir_name[3]],passwd[dir_name[2]]
infile.close()


