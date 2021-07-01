# -*- coding: utf-8 -*-
import numpy as np
#import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt
f=open('dataset.txt','r')
a=f.readline()
arr=[]
g=0
a=a.split(',')
for i in range(0,len(a)):
            arr.append([])
            arr[i].append(a[i])
for line in f:
    line=line.split(',')
    g=g+1
    if g<50001:
        for i in range(0,len(line)):
            #arr.append([])
            if i!=len(a)-1:
                arr[i].append(float(line[i]))
            elif i==len(a)-1:
                y=line[i]
                arr[i].append(float(y[:len(y)-1]))
b=[]
for i in range(0,len(a)):#/n removal
    if i<len(a)-1:
        b.append(a[i])
    else:
        w=a[i]
        w=w[:len(w)-1]
        b.append(w)
a=b
def funct(lis):
    print('-------------')
    print(lis[0],'-------------')
    result=[lis[0]]
    clean=[]
    for i in range(1,len(lis)-1):
        if float(lis[i])!=-9.0 and int(lis[i])!=-8.0:#clean data
            clean.append(float(lis[i]))
    clean=np.array([clean])
    print('sum',np.sum(clean))
    result.append(np.sum(clean))
    print('prod',np.prod(clean))
    result.append(np.prod(clean))
    print('mean',np.mean(clean))
    result.append(np.mean(clean))
    print('sum',np.sum(clean))
    result.append(np.sum(clean))
    print('std',np.std(clean))
    result.append(np.std(clean))
    print('var',np.var(clean))
    result.append(np.var(clean))
    print('min',np.min(clean))
    result.append(np.min(clean))
    print('max',np.max(clean))
    result.append(np.max(clean))
    print('argmin',np.argmin(clean))
    result.append(np.argmin(clean))
    print('argmax',np.argmax(clean))
    result.append(np.argmax(clean))
    return(result)
def round1(pe,ss,kk):
    arr0=[pe,ss,kk]
    for i in range(0,3):
        z=arr0[i] 
        z=str(z)
        if z[0]=='-':
            z=str(round(float(z),2))
        else:
            z=str(round(float(z),3))
        arr0[i]=z
    return(arr0)
def clean2(q,w):
    q1=[]
    w1=[]
    for i in range(0,len(q)):
        if float(q[i])!=-9.0 and float(q[i])!=-8.0 and float(w[i])!=-9.0 and float(w[i])!=-8.0 and q[i]!=-9 and w[i]!=-8:
            q1.append(q[i])
            w1.append(w[i])
    xx=[q1,w1]
    return(xx)#x is an array
def clean(arr,a):
    p=[]
    s=[]
    k=[]
    for i in range(0,len(arr)):
          ppp=a[i]
          ppp=ppp[:3]
          pearsons=[ppp]
          spearmans=[ppp] 
          kendalls=[ppp] 
          for x in range(0,len(arr)):
                q=arr[x][1:]
                w=arr[i][1:]
               
                xx=clean2(q,w)#make so returns 2 values in a array
                q=pd.Series(xx[0])
                w=pd.Series(xx[1])
                pe=q.corr(w) 
                ss=q.corr(w, method='spearman')
                kk=q.corr(w, method='kendall')
                arr0=round1(pe,ss,kk)
                pe=arr0[0]#had to do own function 
                pearsons.append(pe[:6])
                ss=arr0[1]
                spearmans.append(ss[:6])
                kk=arr0[2]
                kendalls.append(kk[:6])
                x1=a[x]
                y1=a[i]
                x = np.array(xx[0])
                y = np.array(xx[1])
                plt.xlabel(x1)
                plt.ylabel(y1)                
                plt.plot(x, y, 'o')
                m, b = np.polyfit(x, y, 1)#ilod only has hours worked for those in ilod 1, working
                plt.plot(x, m*x + b)
                plt.show()
                
              
          p.append(pearsons)
          s.append(spearmans)
          k.append(kendalls)

    for i in range(0,len(a)):
        l=a[i]
        if len(l)<5:
            w=len(l)
            w=5-w# how many short
            l=l+(' '*w)
        a[i]=l[:5] 
    print('pearsons correlation coefficient table')
    print('       ',a)
    for i in range(0,len(p)):
        for x in range(0,len(a)+1):
            o=p[i][x]
            if len(o)<5:
                w=len(o)
                w=5-w# how many short
                p[i][x]=o+(' '*w)
        u=p[i][0]
        p[i][0]=u[:4]
        print(p[i])
    print('spearmans correlation coefficient table')
    print('       ',a)
    for i in range(0,len(s)):
        for x in range(0,len(a)+1):
            o=s[i][x]
            if len(o)<5:
                w=len(o)
                w=5-w# how many short
                s[i][x]=o+(' '*w)
        u=s[i][0]
        s[i][0]=u[:4]
        print(s[i])
    print('kendalls correlation coefficient table')
    print('       ',a)
    for i in range(0,len(k)):
        for x in range(0,len(a)+1):
            o=k[i][x]
            if len(o)<5:
                w=len(o)
                w=5-w# how many short
                k[i][x]=o+(' '*w)
        u=k[i][0]
        k[i][0]=u[:4]
        print(k[i])
 
print('individual comparison')   
result=[['name of class','sum','prod','mean','sum','std','var','min','max','argmin','argmax']]
for i in range(0,len(arr)):
    result.append(funct(arr[i]))
graphdata=[]
gg=[]
g=[]
for i in range(2,len(result)):#ignore casenew as drags graph up too much
    #print(result[i][3])
    graphdata.append(result[i][3])
    mm=a[i-1]
    #print(mm)
    g.append(i)
    mm=str(i)+'='+mm[:3]
    gg.append(mm)
print('key for graph   ',gg)
plt.plot(g,graphdata)#data on the means across the measures
plt.show()
compare=[]
clean(arr,a)


