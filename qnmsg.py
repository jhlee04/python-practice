#!/usr/bin/env python

import subprocess  
import re 

def passwd(): 
    ignore = ('nfsnobody')
    infile = open("/etc/passwd", 'r') 
    lines =  infile.readlines()
    # declare empty dictionary
    passwd = { }          
    for line in lines:
        field=line.split(":")
	user, userid, userdir = field[0], field[2], field[5]
        
	# system and ignore user 
	if int(userid) < 500 or user in ignore: 
		continue	

	match = re.search('(.*)/(\w+)$', userdir)
	if match: 	
		homedir = match.group(1)
		if homedir not in passwd: 
			passwd[homedir] = [] 
	        passwd[homedir].append(user)    
    infile.close()
    return passwd 
    
def df(): 
    cmd = "df -B G" 
    f= subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE) 
    f.stdout.readline()
    size = {} 
    for line in f.stdout.readlines():
        size [ line.split()[-1] ] = line.split()[1][:-1]  
    return size 

def du(usrdir):
    cmd = "du -sBG" + " " + usrdir 
    f= subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE) 
    usage = f.stdout.readline().split()[0][:-1] 
    return usage

