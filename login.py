#!/usr/bin/python
import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
page=''
if 'user' in form and 'pw' in form:

else:
    page='''
<html>
<head>
<title>Whoops!</title>
</head>
<body>
Please enter a username and password.
</body>
</html>'''
    print page

##print ('Content-Type:text/html\n')
def logIn(username, passw):
        f=open('./data/registered.txt', 'r')
        read=f.read()
        if read.find(username+','+passw)==-1:
                print ('WRONG FLUBBING PASSOWRD OR USERNAME')
        else:
                print('Yay! It worked!')
        #else should link to home page with username and data
        f.close()
def register(username, passw):
        f=open('./data/registered.txt', 'r')
        read=f.read()
        f.close()
        newfile=read+'\n'+username+','+passw
        f=open('./data/registered.txt', 'w')
        f.write(newfile)
        f.close()
