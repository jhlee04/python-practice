#!/usr/bin/env python

import subprocess  

def du(usrdir):
    cmd = "du -sBG" + " " + usrdir 
    f= subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE) 
    usage = f.stdout.readline().split()[0][:-1] 
    return usage

