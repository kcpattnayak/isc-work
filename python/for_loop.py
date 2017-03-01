mylist = [23,'hi',2.4e-10]
mylist1 = range(1,1000,3)
for item in mylist:
   print item, mylist.index(item)
for x in mylist1:
   if 20<x<500 and x%2==0:
       print x
   else:
       print 'not found'
