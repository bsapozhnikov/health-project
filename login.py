#!/usr/bin/python
import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()
page='Content-Type: text/html\n\n'

def logIn(username, passw):
        f=open('./data/registered.txt', 'r')
        read=f.read()
        if read.find(username+','+passw)==-1:
                
                f.close()
                return False
        else:
                
                f.close()
                return True


##print ('Content-Type:text/html\n')

#IMPORTANT: STORING CONVENTION FOR FRIENDS IN FRIENDS.TXT:
#username- list of friends, space separated
#Convention for data (where user bios ar kept)
#username---- Whatever the user inputs ----

def getData(username):
        ans=''
        f=open('./data/data.txt', 'r')
        read=f.read()
        q=read.find(username+'----')
        i=read.find('----',q+len(username+'----'))
        cow=read[q+len(username+'----'):i]
        for s in cow:
                if s=='\n':
                        ans+='<br>'
                else:
                        ans+=s 
        f.close()
        return ans

def listFriends(username):
    f=open('./data/friends.txt', 'r')
    ans=""
    read=f.read()
    q=read.find(username+'-')
    i=read.find('\n',q)
    cow=read[q+len(username+'-'):i]
    for s in cow:
        if s==' ':
            ans+='<br>'
        else:
            ans+=s
    f.close()
    return ans

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
    
def register(username, passw):
    f=open('./data/registered.txt', 'r')
    read=f.read()
    f.close()
    thing=''
    thing=''+read+'\n'+username+','+passw
    f=open('./data/registered.txt', 'w')
    f.write(thing)
    f.close()
    f=open('./data/friends.txt', 'r')
    read=f.read()
    f.close()
    snork=read+'\n'+username+'-'
    f=open('./data/friends.txt', 'w')
    f.write(snork)
    f.close()
    f=open('./data/data.txt', 'r')
    read=f.read()
    s1=read+'\n'+username+'----No entry made yet.----'
    f.close()
    f=open('./data/data.txt', 'w')
    f.write(s1)
    f.close()
def editData(username,newdata):
    f=open('./data/data.txt', 'r')
    read=f.read()
    q=read.find(username+'----')
    i=read.find('----',q+len(username+'----'))
    s1=read[:q]
    s2=read[i:]
    s1=s1+username+'---- '+newdata+s2
    f.close()
    f=open('./data/data.txt', 'w')
    f.write(s1)
    f.close()


def makepage(username,passw):
        global page
        if logIn(username,passw):   
                page+='''
<!--read this in with python and alter it as needed to create the home page-->

<!--replace ***** with username in python in order to preserve identity throughout site-->



<html>

  <head>

    <title> 'Sup </title>
    <link rel="stylesheet" type="text/css" href="style.css">

  </head>

  <body>

    <div id="sidebar">

      <h1>Friends</h1>
      '''+listFriends(username)+'''
    </div>

    <div id="main">

      

	  

      <div class="box">

	<div class="name"> Name:'''+username+'''</div>

	<div class="info">'''+getData(username)+'''</div>

      </div>

      

      

    </div>

  </body>

</html>

'''
                print page

        else:
                page+='''
<html>
<head>
<title>Whoops!</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
Please enter a valid username and password.
</body>
</html>'''
                print page

if 'user' in form and 'pw' in form:
        user = form['user'].value
        pw = form['pw'].value
        makepage(user,pw)
else:
        page+='''
<html>
<head>
<title>Whoops!</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
Please enter a valid username and password.
</body>
</html>'''
        print page
