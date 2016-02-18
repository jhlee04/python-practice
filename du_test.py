#!/usr/bin/env python
import os
import sys
from pprint import pprint 
from test_passwd import passwd  

cmd = "du -sBG"

if os.geteuid()  != 0  : 
   print "You are not root" 
   sys.exit()  

usage ={}
for k in passwd.keys() : 
       print 'in ',k  ,"scanning"
   for i in passwd.get(k) : 
       print i ," --> ", 
       dir =  k +i  
       ccmd = cmd + " " + dir  
       s=os.popen(ccmd).readline().split() 
       usage[s[-1]] = s[-2]
print "*end*"     

#os.system(cmd ) 
print " The size of the users   "  
print " user          :  usage  "  
for key in usage.keys() : 
    print key.ljust(15)+":  "+usage[key].ljust(15) 
