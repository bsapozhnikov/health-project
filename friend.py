#!/usr/bin/python
import cgi, cgitb
cgitb.enable()
form = cgi.FieldStorage()
user=form['user'].value
friend=form['friend'].value
pw=form['pw'].value

##def addFriend(user1,user2):
##    f=open('./data/friends.txt', 'r')
##    read=f.read()
##    q=read.find(user1+'-')
##    i=read.find('\n',q)
##    s1=read[:i]
##    s2=read[i:]
##    s1=s1+' '+user2+s2
##    f.close()
##    f=open('./data/friends.txt', 'w')
##    f.write(s1)
##    f.close()

def addFriend(user1,user2):
    f=open('./data/friends.txt','r')
    g=f.read().splitlines()
    ans=''
    for line in g:
        L=line.split('-')
        if L[0] == user1:
            s=' '+user2
            if len(L)>1:
                L[1]=L[1]+s
            else:
                L.append(s)
        ans=ans+'-'.join(L)
        ans+='\r\n'
    
    f.close()
    f2=open('./data/friends.txt','w')
    f2.write(ans)
    f2.close()
        

addFriend(user,friend)
page='Content-Type: text/html\n\n'
page+='''<html>
<head>
<title> 'Sup </title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div class="box">
    Congrats, you have a new friend!<br>
    <form action="login.py" method="post">
      <input type="hidden" name="pw" value="'''+pw+'''">
      <input type="hidden" name="user" value="'''+user+'''">
      <input type="submit" value="Finish" name="Finish">
    </form></body></html>'''
    #Note: you might want to change the submit type if you want it to instantly
#jump between friend and login. See three lines above.
print (page)
