#create a linked list from scratch

class node(object):
    def __init__(self,value):
        self.next=None
        self.value=value

class linkedList(object):
    #def __init__(self):

     def AddToLinkedList(self,n,head):
         if (head.next==None):
             head.next=n
         else:
             n.next=head.next
             head.next=n
   
     def PrintLinkedListHeadFirst(self,head):
         print "\n\nprint head first"
         nodeOut=head
         while(nodeOut.next != None):
             nodeOut=nodeOut.next
             print nodeOut.value,

     def PrintLinkedListTailFirst(self,head):
         print "\n\nprint tail first"
         temp=node(None)
         nodeOut=head
         while (head.next != temp.next):
             while (nodeOut.next != temp.next):
                 nodeOut=nodeOut.next
             print nodeOut.value,
             temp.next=nodeOut
             nodeOut=head         
         
     def GetListLength(self,head):
         nodeOut=head
         count=0
         while (nodeOut.next != None):
             nodeOut=nodeOut.next
             count=count+1
         print "\n\nget number of elements in the list :",count

     def AddElementAtLocation(self,head,location,n):
         print "\n\nadd element at said location i.e. :",location
         count=0
         nodeOut=head
         while (nodeOut.next != None):
             prev=nodeOut
             nodeOut=nodeOut.next
             if (count == (location-1)):
                 print "Location found :",count
                 print "Element at current location is :",nodeOut.value
                 print "Element at previous location is :",prev.value
                 print "inserting now"
                 prev.next=n
                 n.next=nodeOut
                 break
             count=count+1

     def DeleteElementAtLocation(self,head,location):
         print "\ndelete element at said location i.e. : ",location
         count=0
         nodeOut=head
         while (nodeOut.next != None):
             prev=nodeOut
             nodeOut=nodeOut.next
             if (count == (location-1)):
                 print "Location found :",count
                 print "Element that is going to be deleted :",nodeOut.value
                 prev.next=nodeOut.next
                 break
             count=count+1
         
     def ReverseList(self,head):
         print "\nreverse list"
         nodeOut=head
         temp=node(None)
         newHead=node(None)
         while (head.next != temp.next):
            nodeOut=head
            while (nodeOut.next != temp.next):
                 prev=nodeOut
                 nodeOut=nodeOut.next
                 if (nodeOut.next == None):
                     newHead.next=nodeOut
            temp.next=nodeOut
            nodeOut.next=prev
            if(head.next == prev):
                prev.next=None
                break
         return newHead
             
l=linkedList()
head=node(None)

for i in range(1,11):
    a=node(i*10)
    l.AddToLinkedList(a,head)

l.PrintLinkedListHeadFirst(head)
l.PrintLinkedListTailFirst(head)
l.PrintLinkedListHeadFirst(head)
l.GetListLength(head)

n=node(55)
l.AddElementAtLocation(head,3,n)
l.PrintLinkedListHeadFirst(head)
print ""

l.DeleteElementAtLocation(head,4)
l.PrintLinkedListHeadFirst(head)
print ""

head=l.ReverseList(head)
l.PrintLinkedListHeadFirst(head)
print ""

