#!/usr/bin/python
import cgi, cgitb
cgitb.enable()

form=cgi.FieldStorage()
page='Content-type: text/html\n\n'
f1=open('registerformtemplate.html','r')
g1=f1.read()
user = ""
if 'user' in form:
    user = form['user'].value

g1=g1.replace("**user**",user)
page+=g1
print page    
