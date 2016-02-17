#!/usr/bin/env python
from pprint import pprint 

infile = open("/etc/passwd", 'r') 
lines =  infile.readlines()
passwd = { }  #  declare empty dictionary
dir_name = ('/home','/home2','/users/nst551')
home = [] 
home2 = [] 
users = [] 


for dir in dir_name : 
    passwd[dir] = []  

for line  in lines:
    item=line.split(":")

    if int(item[2]) > 500 :
        dir = item[5].split("/")[1]
        if dir == 'home' :
            home.append(item[0]) 
        elif dir == 'home2' :
            home2.append(item[0]) 
        elif dir == 'users' :
            users.append(item[0]) 

passwd['/home'].append(home)
passwd['/home2'].append(home2)
passwd['/users/nst551'].append(users)

pprint(passwd)  

infile.close()


