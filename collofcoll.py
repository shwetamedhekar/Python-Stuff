'''
@Description: This is to create an iterator to step through a collection of collection without using the "yield" keyword.
                      (Anything other than dict as dict will work as dict is a index:value)
@Author: Shweta Medhekar
@Created Date: Feb 2011
'''
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


