#!C:\Program Files\Python311\python.exe
import cgi, numpy as np
print("Content-type: text/html")

form = cgi.FieldStorage( )

reshtml='''Content-Type:text/html\n
<HTML>
<head>
<title>
Res2
</title>
</head>
<body>
<h3>N: <i>%s</i></h3>
M: <b>%s</b>
Mim: <b>%s</b>
Pos: <b>%s</b>
Sum<b>%s</b>
</body>
</HTML>'''

n = form.getvalue("n")
m=[n][n]

s=list(form.getvalue("s"))

m=np.array(s)

#st = form['s'].value
#m={{1,2,3},{4,5,6},{7,8,9}}

min = 100
pos=0
sum=0

for i in m:
    for j in i:
        if j<min:
            min=j
            pos=i

for i in m:
    if i==pos:
        for j in i:
            sum+=j




print(reshtml % (n, m, min,pos,sum))


