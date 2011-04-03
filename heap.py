#there is a package heapq that can be directly used

#heap - starts with x[1]
#left -> 2i
#right -> 2i+1

from random import randint
import sys

def siftup(a):
    n=len(a)
    i=n-1
    while (i > 1):
        if(a[i] < a[i/2]):
            tmp=a[i/2]
            a[i/2]=a[i]
            a[i]=tmp
        i=i/2
    return a

def siftdown(a):
    i=1
    n=len(a)
    while((2*i + 1) < n):
        if((a[i] > a[2*i]) or (a[i] > a[2*i + 1])):
            if(a[2*i] < a[2*i + 1]):
                tmp=a[i]
                a[i]=a[2*i]
                a[2*i]=tmp
                i=2*i
            else:
                tmp=a[i]
                a[i]=a[2*i + 1]
                a[2*i + 1]=tmp
                i=2*i + 1
        else:
            break
    if (2*i < n):
        if(a[2*i] < a[i]):
            tmp=a[i]
            a[i]=a[2*i]
            a[2*i]=tmp
    return a
            

def main():
    x=[]
    x.append(0)
    #x=[0]*11

    print "Create heap with siftup"
    for i in range(0,10):
        x.append(randint(0,100))
        x=siftup(x)

    print "Heap : ", x, len(x)

    print "\nPriority queue with siftdown -- heap sort"
    while (len(x)>1):
        temp=x[len(x)-1]
        x[len(x)-1]=x[1]
        x[1]=temp
        print x.pop()
        x=siftdown(x)
        #print "Heap : ", x, len(x)


if __name__ == "__main__":
    sys.exit(main())




