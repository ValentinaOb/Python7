#C:\Users\user\AppData\Local\Programs\Python\Python312\python.exe
#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()

    
one = int(form.getfirst('one',2))
two = int(form.getfirst('two',6))
three = int(form.getfirst('three',5))


if((one +two)>three) and (one +three)>two and (three +two)>one:
    s = True
else: 
    s = False

print("Content-type: text/html\n\n")

form = cgi.FieldStorage()


print("<html>")
print("<head>")
print("<title>Success Page</title>")
print("</head>")
print("<body>")

print("<h2>Sides </h2>")
print("<p>One: <strong><span style='font-size: 20px;'>{}</span></strong> </p>".format(one))
print("<p>Two: <strong><span style='font-size: 20px;'>{}</span></strong> </p>".format(two))
print("<p>Three: <strong><span style='font-size: 20px;'>{}</span></strong> </p>".format(three))

print("<br>")

print("<p>one +two: <strong><span style='font-size: 20px;'>{}</span></strong> </p>".format((one +two)))
print("<p>one +three: <strong><span style='font-size: 20px;'>{}</span></strong> </p>".format(one +three))
print("<p>three +two: <strong><span style='font-size: 20px;'>{}</span></strong> </p>".format(three +two))


if((one +two)>three) and (one +three)>two and (three +two)>one:
    print("<p style='font-size: 25px;'>Triangle: Yes</p>")
else: 
    print("<p style='font-size: 25px;'>Triangle: No</p>")


print("</body>")
print("</html>")
