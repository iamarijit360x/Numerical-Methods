# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:07:58 2022

@author: Arijit Banerjee
"""

#"{0:>5}".format(i)
global ss
def func(x):
    return eval(ss)

def intarr():
    i=0
    n=False
    p=False
    arr=[0,0]
    while True:
        t=func(i)
        if(t>0):
            arr[1]=i
            p=True
        elif(t<0):
            arr[0]=i
            n=True
        
        if(n and p):
            return arr
        i=i+1
        
prev=[0,0,0]
p=int(input("Precision:"))
ss=input("Enter f(x):")
arr=intarr()
a=arr[0]
b=arr[1]
i=0

while True:
    
    fa=func(a)
    fb=func(b)
    c=(a*fb - b*fa)/(fb-fa)
    fc=func(c)
    print("{0:>7}".format(i),"{0:>7}".format(round(a,6)),"{0:>7}".format(round(b,6)),"{0:>7}".format(round(c,6)),"{0:>7}".format(round(fc,6)))
    if(fc>0):
        b=c
    else:
        a=c
    if(prev[0]==round(a,p) and prev[1]==round(b,p) and prev[2]==round(c,p)):
        break
    prev[0]=round(a,p)
    prev[1]=round(b,p)
    prev[2]=round(c,p)
    i=i+1
    