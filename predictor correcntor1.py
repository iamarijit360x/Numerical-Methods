def func(x,y,ss):
    return eval(ss) #CHNAGE THE FUNCTION F(x,y) or dy/dx
f=[]
xarr=[]
yarr=[]
prc=int(input("Precision:"))
ss=input("Enter Funcion:")
h=float(input("Enter Value of h(step):"))
xint=float(input("x0:"))

for i in range(4):
    x=xint+i*h
    y=float(input(f"Y{i}:"))
    fxy=func(x,y,ss)
    xarr.append(x)
    yarr.append(y)
    f.append(fxy)
print("N        X           Y               Z")
for i in range(len(xarr)):
    print(i,xarr[i].ljust(20),yarr[i],f[i])

p=yarr[0]+(4/3)*h*(2*f[1]-f[2]+2*f[3])
xarr.append(xarr[3]+h)
f.append(func(xarr[4],p,ss))
cprev=0;

itr=0;
while(True):
    c=yarr[2]+(1/3)*h*(f[2]+4*f[3]+f[4])
    ct=func(xarr[4],c,ss)
    if(round(c,prc)-round(cprev,prc)==0):
        break
    cprev=c
    f[4]=ct
    itr+=1
print(c,itr)