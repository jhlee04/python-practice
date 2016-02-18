#!/usr/bin/env python
import os 
cmd = "df -B G" 
#os.system(cmd ) 
f= os.popen(cmd) 
f.readline()
print " The size of the partition  "  
for line in f.readlines(): 
    print line.split()[-1]  , ' : ', line.split()[-3][:-1]
