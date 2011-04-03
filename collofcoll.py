#collection of collection. Anything other than dict as dict is index:value
#only problem with code is infinite loop if same elment present in contiguous locations

import sys

class myIterator(object):
    def __init__(self,object):
        self.current=None #class variable or ptr to the current position so can be done w/o 'yield"

    def my_next(self):
        toreturn=0
        for inner in c:
             for obj in inner:
                if ((toreturn==1) or (self.current==None)):
                    self.current=obj
                    return obj
                if (obj==self.current):
                    toreturn=1


c=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

    # h=[1,2,3,4,5]
    # k=[6,7,8,9,10]
    # c=zip(h,k)

print c
a=myIterator(c)

while True:
    try:
        value = a.my_next()
        if (value==None):
            break
        else:
            print "value : ",value
    except:
        break


