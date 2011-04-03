#Merge sort

from random import randint
import sys


def merge_sort(x):
    if (len(x)==1):
        return x
    a=[]
    b=[]
    for i in range(0, len(x)/2):
        a.append(x[i])

    for i in range(len(x)/2, len(x)):
        b.append(x[i])

    a_back=merge_sort(a)
    b_back=merge_sort(b)

    merged=[]
    j=0
    k=0
    for i in range (0,(len(a_back)+len(b_back))):
        if((j<len(a_back)) and (k<len(b_back))): 
            if(a_back[j] < b_back[k]):
                merged.append(a_back[j])
                j=j+1
            else:
                merged.append(b_back[k])
                k=k+1
        elif(j<len(a_back)):
            merged.append(a_back[j])
            j=j+1
        else:
            merged.append(b_back[k])
            k=k+1

    return merged

def main():        
    input_num=[]
    for i in range (10):
        input_num.append(randint(0,100))
    print input_num, len(input_num)

    output_num=merge_sort(input_num)
    print output_num, len(output_num)


if __name__ == "__main__":
    sys.exit(main())
