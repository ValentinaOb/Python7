import cgi
form = cgi.FieldStorage( )

print ("Content−type: text /html")
#one = form.getfirst("one",2)
#two = form.getfirst("two",6)
#three = form.getfirst("three",5)
one = form.getvalue('one')
two = form.getvalue('two')
three = form.getvalue('three')


if((one +two)>three) and (one +three)>two and (three +two)>one:
    s = True
else: 
    s=False

print("<html>")
print("<head>")
print("<title>Result</title>")
print("</head>")
print("<body>")
print("<h2>Registration Confirmation</h2>")
print("<p>One: " + one + "</p>")
print("<p>Two: " + two + "</p>")
print("<p>Three: " + three + "</p>")

print("<h3>Triangle: " + s + "</h3>")

print("</body>")
print("</html>")

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