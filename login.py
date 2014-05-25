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
def otherData(username,password):
        ans=''
        f=open('./data/data.txt','r')
        g=f.read().splitlines()
        f2=open('./data/friends.txt','r')
        g2=f2.read().splitlines()
        D2={}
        for line in g2:
                L=line.split('- ')
                if len(L)>1:
                        L1 = L[1].split(' ')
                        ##L[0] is name; L1 is list of friends
                        D2[L[0]]=L1
                else:
                        D2[(L[0])[:-1]]=[]
        for line in g:
                L=line.split('----')
                ##L[0] is name; L[1] is aboutme
                ans+='''
      <div class="box">

	<div class="name"> Name:'''+L[0]+'''</div>

	<div class="info">'''+L[1]+'''</div>'''
                ans+='\n<!--L[0]='+L[0]+', username='+username+', D2[L0]='+`D2[L[0]]`+' -->'
                if (L[0] != username) and (L[0] not in D2[username]):
                        ans+='''
                        <form action="friend.py" method="post">

                           <input type="hidden" name="user" value="'''+username+'''">
                           <input type="hidden" name="friend" value="'''+L[0]+'''">
                           <input type="hidden" name="pw" value="'''+password+'''">
                           <input type="submit" value="Add Friend" name="friend">

                        </form>'''
                ans+='''
      </div><br>\n'''
        return ans
def listFriends(username):
    f=open('./data/friends.txt', 'r')
    ans=''
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

    <div id="sidebar" class="box">

      <h1>Friends</h1>
      '''+listFriends(username)+'''
    </div>

    <div id="main">'''
                               
        
      

                	  
##                page+='''
##      <div class="box">
##
##	<div class="name"> Name:'''+username+'''</div>
##
##	<div class="info">'''+getData(username)+'''</div>
##
##      </div>'''

                page+=otherData(username,passw)

      
                page+='''
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
