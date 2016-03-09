#!/usr/bin/env python

import subprocess  
from pprint import pprint 

def df(): 
    cmd = "df -B G" 
    f= subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE) 
    f.stdout.readline()
    size = {} 
    for line in f.stdout.readlines():
        size [ line.split()[-1] ] = line.split()[1][:-1]  
    return size 

