import turtle
import time

sc=turtle.Screen()
sc.bgcolor("white")
sc.title("Horse Run")

k=turtle.Turtle()
k.color("black")
k.width(5)
k.speed(500)
k.penup()
k.goto(-248,250)
k.penup()
k.width(5)
g=-50

turtle.register_shape("horse.gif")
hor=[]
a=turtle.numinput('rows','prompt')
b=turtle.numinput('columns','prompt')

h=int(b)*50
hh=int(a)*50
l=[]
for i in range(int(a)):
    p=turtle.textinput('Values','prompt')
    l.append(p.split(" "))
ll=[]
for i in l:
    m=[]
    for j in i:
        if(int(j)>int(a) and int(j)>int(b)):
            turtle.done()
        m.append(int(j))
    ll.append(m)
for i in range(int(a)+1):
    k.goto(-248,g)
    k.pendown()
    k.forward(h)
    k.penup()
    g=g+50
p=-248
k.right(270)
for j in range(int(b)+1):
    k.goto(p,-50)
    k.pendown()
    k.forward(hh)
    k.penup()
    p=p+50
k.penup()
gg=60
f=p
p=hh-80
k.goto(0,p-50)

i=int(a)-1
j=int(b)-1
c=0
d=0
f=[]
while(i>0 or j>0):
    s=ll[i][j]
    print(s,i,j)
    if(s==0):
        d=1
        break
    ss=s
    print(i,j)
    p=i
    q=j
    while(s>0):
        s=s-1
        p=p-1
    while(ss>0):
        ss=ss-1
        q=q-1
    if(q<0):
        if(ll[p][j]>0):
            i=p
            j=j
        else:
            i=p
            j=0
    elif(p<0):
        if(ll[i][q]>0):
            i=i
            j=q
        else:
            i=0
            j=q
    else:
        if(ll[p][j]>=ll[i][q] ):
            i=p
            j=j
            print("here")
        else:
            i=i
            j=q
    c=c+1
    f.append([i,j])
f.append([int(a)-1,int(b)-1])
k.hideturtle()
tt=100
p=hh-80
for i in range(int(a)):
    tt=100
    for j in range(int(b)):
        k.goto(tt,p)
        k.write(ll[i][j],font=("candra",16,"bold"))
        tt=tt+50
    p=p-50
k.hideturtle()
gg=60
p=hh-80
k.goto(0,p-50)
turtle.penup()
k.penup()
for i in range(int(a)):
    o=-230
    for j in range(int(b)):
        time.sleep(1.025)
        uu=0
        for w in f:
            if w[0]==i and w[1]==j:
                uu=1
                break
        if(uu==1):
            uu=0
            turtle.goto(o,p)
            hor.append([o,p])
            k.goto(o,p)
            k.hideturtle()
            k.write("__")
            k.hideturtle()
            
        else:
            k.goto(o,p)
            k.write((ll[i][j]),font=("candra",16,"bold"))
            k.hideturtle()
        o=o+50
    gg=gg-50
    p=p-50

hor=hor[::-1]
print(hor)
for i in hor:
    turtle.goto(i[0],i[1])
    turtle.shape("horse.gif")
    time.sleep(1.5)
    
if(d==1):
    k.goto(-230,-200)
    k.write("There is no route to reach the destination",font=("candra",16,"bold"))
else:
    k.goto(-230,-200)
    k.write(" Destination Reached Successfully..!",font=("candra",16,"bold"))
  
k.hideturtle()
    
