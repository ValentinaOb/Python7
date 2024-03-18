#!C:\Users\user\AppData\Local\Programs\Python\Python312\python.exe

import cgi
form = cgi.FieldStorage()

    
n = int(form.getfirst('n',2))
text = str(form.getfirst('s',"1 2 3 4"))

#n=3
#text = "1 2 3 4 5 6 7 8 0"

t1=text.split(" ")

#a = [[]*n]*n

a = ([t1[i: i + n] for i in range(0, len(t1), n)])
a = [list( map(int,i) ) for i in a] 

#a = [list(ele) for ele in t]
#res = list(map(lambda ele: list(ele), text))

'''
a=[]
l=0
for i in range(n):
    col = []
    for j in range(n):
        for k in t:
            if l==n: break
            col.append(k)
            l+=1
        l=0
    a.append(col)
'''

'''
for k in t:
    for i in a:
        for j in i:
            a[i][j]=int(k)
'''
min = 100
pos=0
sum=0

for i in a:
    for j in i:
        if j<min:
            min=j
            pos=i

for i in a:
    if i==pos:
        for j in i:
            sum+=j


print("Content-type: text/html\n\n")

form = cgi.FieldStorage()


print("<html>")
print("<head>")
print("<title>Success Page</title>")
print("</head>")
print("<body>")

print("<h2>Data </h2>")
print("<p>N: <strong><span style='font-size: 20px;'>{}</span></strong> </p>".format(n))
print("<p>M: <strong><span style='font-size: 20px;'>{}</span></strong> </p>".format(text))

print("<br>")

print("<p>Min: <strong><span style='font-size: 20px;'>{}</span></strong> </p>".format(min))
print("<p>Row: <strong><span style='font-size: 20px;'>{}</span></strong> </p>".format(pos))
print("<p>Sum: <strong><span style='font-size: 20px;'>{}</span></strong> </p>".format(sum))


print("</body>")
print("</html>")
