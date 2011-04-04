'''
@Description: Create a binary tree and run some functions to traverse, get succesor, get predecessor, find element, add element
@Author: Shweta Medhekar
@Created Date: Feb 2011
'''

from random import randint

class node(object):
    def __init__(self,value):
        self.value=value
        self.leftChild=None
        self.rightChild=None
        self.parent=None

class binaryTree(object):

    def AddNodeToTree(self,n,root):
        ptr=root
        if (ptr.value == None): #this implies that the tree is empty and this is the first element being entered.
            print "this is the root"
            root=n
            return root

        while True:
            if (n.value <= ptr.value):
                if(ptr.leftChild != None):
                    ptr=ptr.leftChild
                else:
                    print "location found 'left child'"
                    ptr.leftChild=n
                    n.parent=ptr
                    break
            
            if (n.value > ptr.value):
                if(ptr.rightChild != None):
                    ptr=ptr.rightChild
                else:
                    print "location found 'right child'"
                    ptr.rightChild=n
                    n.parent=ptr
                    break
        return root

        
    def FindElement(self,root,val):
        if(root.value==val):
            print "Element found !"
            return root 

        if(val < root.value):
            if (root.leftChild != None):
                return b.FindElement(root.leftChild,val)
            else:
                print "Element not in tree "
        
        if(val > root.value):
            if (root.rightChild != None):
                return b.FindElement(root.rightChild,val)
            else:
                print "Element not in tree "
        
        
    def InOrderTraversal(self,tmp):
        if(tmp.leftChild != None):
            b.InOrderTraversal(tmp.leftChild)
        print tmp.value,
        if(tmp.rightChild != None):
            b.InOrderTraversal(tmp.rightChild)

            
    def FindMinimum(self,tmp):
        if(tmp.leftChild != None):
            return b.FindMinimum(tmp.leftChild)
        else:
            print "min element found"
            return tmp


    def FindMaximum(self,tmp):
        if(tmp.rightChild != None):
            return b.FindMaximum(tmp.rightChild)
        else:
            print "max element found"
            return tmp

        
    def FindSuccessor(self,root,val):
        print "get the successor"
        found=b.FindElement(root,val)
        if (found != None):
            print "Said node is present in the tree : ",found.value, found.leftChild, found.rightChild, found.parent

#CASE 1 : If the said element has a right child, then the minimum of the right sub tree is the successor
            if (found.rightChild != None):
                print "successor found"
                found=b.FindMinimum(found.rightChild)
                return found
#CASE 2 : If said element has no right child, go up the tree till condition current element is left child. That parent is the successor
            else:
                ancestor=found.parent
                while ((ancestor.rightChild == found)and(ancestor != None)):
                    found=ancestor
                    if(ancestor.parent != None):
                        ancestor=ancestor.parent
                    else:
                        print "this element has no successor"
                        ancestor=None
                        break
                return ancestor
        else:
            print "Element does not exist - sucessor cannot be found"
            return None


    def FindPredecessor(self,root,val):
        print "get the predecessor"
        found=b.FindElement(root,val)
        if (found != None):
            print "Said node is present in the tree : ",found.value, found.leftChild, found.rightChild, found.parent

#CASE 1 : If the said element has a left child, then the max of the left sub tree is the predecessor
            if (found.leftChild != None):
                print "predecessor found"
                found=b.FindMaximum(found.leftChild)
                return found
#CASE 2 : If said element has no left child, go up the tree till condition current element is right child. That parent is the successor
            else:
                ancestor=found.parent
                while ((ancestor.leftChild == found)and(ancestor != None)):
                    found=ancestor
                    if(ancestor.parent != None):
                        ancestor=ancestor.parent
                    else:
                        print "this element has no predecessor"
                        ancestor=None
                        break
                return ancestor
        else:
            print "Element does not exist - predecessor cannot be found"
            return None


#CASE 1 : If node to be removed has no children. Simply remove. Does not affect tree.
#CASE 2 : If node to be removed has 1 child, child gets connected to parent of node being removed.
#CASE 3 : If node has 2 children. Replace node by its successor (this will have 1 child). Now make the successor tree valid by applying case 1 and 2 to the successor.
    def RemoveNodeFromTree(self,root,val):
        print "function to remove node"
        found=b.FindElement(root,val)
        if (found != None):
            print "Said node is present in the tree : ",found.value#, found.leftChild, found.rightChild, found.parent
            if((found.leftChild==None) and (found.rightChild==None)): #no children
                print "no chlidren"
                tmp_parent=found.parent
                if(tmp_parent.leftChild==found):
                    tmp_parent.leftChild=None
                else:
                    tmp_parent.rightChild=None
                found.value=None
                found.parent=None
            elif((found.leftChild==None) or (found.rightChild==None)): #1 child
                print "1 child"
                tmp_parent=found.parent
                if (found.leftChild != None):
                    tmp_child=found.leftChild
                else:
                    tmp_child=found.rightChild
                if (tmp_parent.leftChild==found):
                    tmp_parent.leftChild=tmp_child
                    tmp_child.parent=tmp_parent
                    found.leftChild=None
                    found.rightChild=None
                    found.parent=None
                    found.value=None
                else:
                    tmp_parent.rightChild=tmp_child
                    tmp_child.parent=tmp_parent
                    found.leftChild=None
                    found.rightChild=None
                    found.parent=None
                    found.value=None
            else: #two children...messy
                print "2 children get successor to replace"
                tmp_succ=b.FindSuccessor(root,found.value)
                print "successor : ",tmp_succ.value
                if((tmp_succ.leftChild==None) and (tmp_succ.rightChild==None)): #no children
                    print "no child"
                    tmp_parent=tmp_succ.parent
                    if(tmp_parent.leftChild==tmp_succ):
                        tmp_parent.leftChild=None
                    else:
                        tmp_parent.rightChild=None
                else:#((tmp_succ.leftChild==None) or (tmp_succ.rightChild==None)): #1 child
                    tmp_parent=tmp_succ.parent
                    if (tmp_succ.leftChild != None):
                        tmp_child=tmp_succ.leftChild
                    else:
                        tmp_child=tmp_succ.rightChild
                        if (tmp_parent.leftChild==tmp_succ):
                            tmp_parent.leftChild=tmp_child
                            tmp_child.parent=tmp_parent
                        else:
                            tmp_parent.rightChild=tmp_child
                            tmp_child.parent=tmp_parent
                tmp_succ.parent=found.parent
                tmp_succ.leftChild=found.leftChild
                tmp_succ.rightChild=found.rightChild
                if (found.parent != None):
                    tmp_p=found.parent
                    if(tmp_p.leftChild==found):
                        tmp_p.leftChild=tmp_succ
                    else:
                        tmp_p.rightChild=tmp_succ
                else:
                    print "No parent. This is the root."
                    return tmp_succ
                found.parent=None
                found.leftChild=None
                found.rightChild=None
        else:
            print "Node not found in tree. Cannot remove."
        return root

root=node(None)
a=node(5)
b=binaryTree()
root=b.AddNodeToTree(a,root)

#### Adding elements
print "\n------------Adding Elements---------------"
a=node(3)
root=b.AddNodeToTree(a,root)
a=node(10)
root=b.AddNodeToTree(a,root)
a=node(12)
root=b.AddNodeToTree(a,root)
a=node(2)
root=b.AddNodeToTree(a,root)
a=node(1)
root=b.AddNodeToTree(a,root)
a=node(8)
root=b.AddNodeToTree(a,root)
a=node(4)
root=b.AddNodeToTree(a,root)
####

print "\n------------In Order Traversal---------------"
b.InOrderTraversal(root)

print "\n------------Find Element----------------"
found=b.FindElement(root,33)
if (found != None):
    print found.value#, found.leftChild, found.rightChild, found.parent
found=b.FindElement(root,1)
if (found != None):
    print found.value#, found.leftChild, found.rightChild, found.parent
found=b.FindElement(root,10)
if (found != None):
    print found.value#, found.leftChild, found.rightChild, found.parent
found=b.FindElement(root,8)
if (found != None):
    print found.value#, found.leftChild, found.rightChild, found.parent

print "\n------------In Order Traversal---------------"
b.InOrderTraversal(root)

print "\n------------Get Minimum Element in tree----------"
tmp=b.FindMinimum(root)
if (tmp != None):
    print tmp.value#, tmp.leftChild, tmp.rightChild, tmp.parent

print "\n------------Get Maximum Element in tree----------"
tmp=b.FindMaximum(root)
if (tmp != None):
    print tmp.value#, tmp.leftChild, tmp.rightChild, tmp.parent

print "\n------------Find successor----------------"
successor=b.FindSuccessor(root,4)
if (successor != None):
    print successor.value#, successor.leftChild, successor.rightChild, successor.parent

print "\n------------Find predecessor----------------"
predecessor=b.FindPredecessor(root,5)
if (predecessor != None):
    print predecessor.value#, predecessor.leftChild, predecessor.rightChild, predecessor.parent

print "\n------------In Order Traversal---------------"
b.InOrderTraversal(root)

print "\n\n------------Remove element----------------"
root=b.RemoveNodeFromTree(root,5)

print "\n------------In Order Traversal---------------"
b.InOrderTraversal(root)


