'''
@Description: Run quick sort on a list of 10 randomly generated numbers.
@Author: Shweta Medhekar
@Created Date: Feb 2011
'''

from random import randint
import sys

def quick_sort(x):
    if(len(x)==1):
        return x
    
    j=0
    while (j<len(x)):
        pivot=x[j]
        a=[]
        b=[]
        for i in range (len(x)):
            if(x[i]<=pivot):
                a.append(x[i])
            else:
                b.append(x[i])
        if(len(a)>0 and len(b)>0):
            break
        j=j+1
        
    if(j<len(x)): #else everything is equal
        if(len(a)>0):
            a=quick_sort(a)
        if(len(b)>0):
            b=quick_sort(b)

    a.extend(b) #join 2 together and return
    return a
        
def main():
    input_num=[]
    for i in range(10):
        input_num.append(randint(0,100))


    print input_num, len(input_num)
    output_num=quick_sort(input_num)
    print output_num, len(output_num)


if __name__ == "__main__":
    sys.exit(main())
