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
page='Content-Type: text/html\n\n'
page+='''<html><body>
Congrats, you have a new friend!<br>
    <form action="login.py" method="post" class="box" id="form">
      <input type="hidden" name="pw" value="'''+pw+'''">
      <input type="hidden" name="user" value="'''+user+'''">
      <input type="submit" value="Finish" name="Finish">
    </form></body></html>'''
    #Note: you might want to change the submit type if you want it to instantly
#jump between friend and login. See three lines above.
print (page)
