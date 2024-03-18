import cgi
form = cgi.FieldStorage( )


reshtml='''Content-Type:text/html\n
<HTML>
<HEAD>
<title>
Friends CGI demo(dynamic screen)
</title>
</HEAD>
<body>
<h3>Friends list for:<i>%s</i></h3>
Your name is: <b>%s</b>
You have<b>%s</b>friends.
</body>
</HTML>'''

one = form['one'].value
two = form['two'].value
three = form['three'].value
print(reshtml % (one, two, three))

#one = int(form['one'])
#two = int(form['two'])
#three = int(form['three'])
'''
one = int(form.getfirst('one',2))
two = int(form.getfirst('two',6))
three = int(form.getfirst('three',5))
'''
#one = form.getvalue('one')
#two = form.getvalue('two')
#three = form.getvalue('three')
'''
print ('One '+one)
print ('Two '+two)
print ('Three '+three)
'''


'''
if((one +two)>three) and (one +three)>two and (three +two)>one:
    s = True
else: 
    s = False
    

print ( "Content−type : text/html\n" )


print('<html>')
print('<head>')
print('<title>Result</title>')
print('</head>')
print('<body>')
print('<h2>Registration Confirmation</h2>')
print('<p>One:  {} </p>'.format(one))
print('<p>Two:  {} </p>'.format(two))
print('<p>Three: {}</p>'.format(three))

print('<h3>Triangle: {} </h3>'.format(s))

print('</body>)')
print('</html>')
'''


'''
print ("One: ", one )
print("Two",two) 
print ("Three: ",three)

if((one +two)>three) and (one +three)>two and (three +two)>one:
    print("\nYes!")
else: 
    print("\nNo")


print("1: ",one)
print("2: ",two)
print("3: ",three)
'''