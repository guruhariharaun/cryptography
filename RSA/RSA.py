

import math
global n
global g
channel=[]
def mod_exp(a,b,m):
    res=1
    while(b>0):
        if(b&1):
            res=res*a%m
        a=a*a%m
        b>>=1
        
    return res    
    
    
def gcd(n,m):
    if(m==0):
        return n
    else: 
        return gcd(m,n%m)
    
    

def cal_phi(n):
    
    result=n
    for i in range(2,math.floor(math.sqrt(n))):
        if(n%i==0):
            while(n%i==0):
                n/=i
            result-=int(result/i)        
    if(n>1):
        result-=int(result/n)
        
    return result

def key_generation():
    public_key=[]
    private_key=[]
    print("input two prime number")
    p=int(input())
    q=int(input())
    private_key.append(p)
    private_key.append(q)
    n=p*q
    g=cal_phi(n)
    channel.append(n)
    public_key.append(n)
    
    e=2
    while(e<g):
        if(gcd(e,g)!=1):
            e=e+1
        else:
            break
    public_key.append(e)        
    d=1
    for i in range(1,g):
        if(e*i%g==1):
            
            d=i
    private_key.append(d)   
    return  private_key,public_key,g,n  
    




global c
x2=1
x1=1
channel=[]
def encryption():
    pri_s,pub_t,false,base=key_generation()
    
    channel.append(pri_s[2])
    print("enter plaintext")
    p=int(input())
    c=mod_exp(p,pub_t[1],base)
    channel.append(c)
    print("element on public channel:")
    print(channel)




def decryption():
    
    retrived_d=mod_exp(int(channel[2]),channel[1],channel[0])
    print(retrived_d)




encryption()
decryption()

