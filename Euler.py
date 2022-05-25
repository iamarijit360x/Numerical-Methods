def func(x,y,ss):
    return eval(ss) #CHNAGE THE FUNCTION F(x,y) or dy/dx
f=[]
xarr=[]
yarr=[]

ss=input("Enter Funcion:")
h=float(input("Enter Value of h(step):"))
x0=float(input("x0:"))
y0=float(input("y0:"))
xarr.append(x0)
yarr.append(y0)
xn=float(input("xn:"))
i=1
x=0
print(f"y({x0})={y0}")
print(f"y({xn})=?")
print("-------------------------------------------------------------")
while(True):
    x=x0+i*h
    print(f"x{i}={x0}+{i}*{h}={x}")
    print("\n")
    xarr.append(x)
    yarr.append(yarr[i-1]+h*func(xarr[i-1],yarr[i-1],ss))
    print(f"y{i}={round(yarr[i-1],5)}+{h}*{round(func(xarr[i-1],yarr[i-1],ss),5)}={round(yarr[-1],5)}")
    print("\n")
    i=i+1
    if(x==xn):
        break
print("-------------------------------------------------------------")
print(f"y[{xn}]={yarr[-1]}")   