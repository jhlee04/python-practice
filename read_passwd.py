#!/usr/bin/env python

infile = open("/etc/passwd", 'r') 
lines =  infile.readlines()
info={}  #  declare empty dictionary

for line  in lines:
    item=line.split(":")
    
    if int(item[2]) > 500 and int(item[2])<600:
        info[item[0]]=[]
	info[item[0]].append(item[5])
print '** user : home directory **'
for x in info : 
     print x,':',info[x][0]

infile.close()


