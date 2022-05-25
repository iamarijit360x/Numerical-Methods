

import sys
def swap(arr,i,n,c):
    if(i+c>=n):
        sys.exit("not possible")
    temp=arr[i]
    arr[i]=arr[i+c]
    arr[i+c]=temp
  
            
    
        

def dd(arr,n,i):
        temp=0
        for j in range(n):
            if(i!=j):
                temp=temp+arr[i][j]
        if(abs(arr[i][i])<temp):
            return False
        return True

def ddint(arr,n):
    for i in range(n):
        c=1
        while(not(dd(arr,n,i))):
              swap(arr,i,n,c)
              c=c+1
             
              
p=int(input("Enter Precison:"))            
arr=[]
n=3
for i in range(3):
    arr.append([float(x) for x in input().split()])
ddint(arr,3)    
print(arr)
x=0
y=0
z=0
prev=[0,0,0]
print("{0:>7}".format('N'),"{0:>7}".format('X'),"{0:>7}".format('Y'),"{0:>7}".format('Z'))
while(True):
    print("{0:>7}".format(i),"{0:>7}".format(x),"{0:>7}".format(y),"{0:>7}".format(z))
    x=round((arr[0][n]-(y*arr[0][1]+z*arr[0][2]))/arr[0][0],p)
    y=round((arr[1][n]-(x*arr[1][0]+z*arr[1][2]))/arr[1][1],p)
    z=round((arr[2][n]-(y*arr[2][1]+x*arr[2][0]))/arr[2][2],p)
    if(x==prev[0] and y==prev[1] and z==prev[2]):
        break
    prev[0]=x
    prev[1]=y
    prev[2]=z
    i=i+1










