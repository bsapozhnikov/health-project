#!/usr/bin/python
import cgi,cgitb
cgitb.enable()

form=cgi.FieldStorage()
page='Content-type: text/html\n\n'

if 'user' in form and 'pw' in form and 'aboutme' in form:
    user=form['user'].value
    pw=form['pw'].value
    aboutme=form['aboutme'].value
    f1=open('data/registered.txt','r')
    g1=f1.read().splitlines()
    f1.close()
    D1={}
    for line in g1:
        if line:
            L=line.split(',')
            D1[L[0]]=L[1]
    if user in D1:
        page+='''
<html>
<head>
<title>Whoops!</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div class="box">
This username has already been taken.
</div>
</body>
</html>'''
        print page
    else:
        ##append data.txt
        r=user+'----'+aboutme+'----\n'
        f2=open('data/data.txt','a')
        f2.write(r)
        f2.close()
        ##append friends.txt
        s=user+'-\n'
        f3=open('data/friends.txt','a')
        f3.write(s)
        f3.close()
        ##append registered.txt
        t=user+','+pw+'\n'
        f4=open('data/registered.txt','a')
        f4.write(t)
        f4.close()
        page+='''
<html>
<head>
<title>Welcome!</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div class="box">
You are registered!
</div>
</body>
</html>'''
        print page
        
else:
    page+='''
<html>
<head>
<title>Whoops!</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div class="box">
Please enter a valid username and password.
</div>
</body>
</html>'''
    print page

