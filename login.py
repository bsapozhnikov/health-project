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
