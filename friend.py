#!/usr/bin/python
import cgi, cgitb
cgitb.enable()
form = cgi.FieldStorage()


def addFriend(user1,user2):
    f=open('./data/friends.txt', 'r')
    read=f.read()
    q=read.find(user1+'-')
    i=read.find('\n',q)
    s1=read[:i]
    s2=read[i:]
    s1=s1+' '+user2+s2
    f.close()
    f=open('./data/friends.txt', 'w')
    f.write(s1)
    f.close()

addFriend(user,friend)
