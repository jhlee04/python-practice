#!/usr/bin/env python

from pprint import pprint 
import re 

ignore = ('nfsnobody')

def passwd(): 
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
    
