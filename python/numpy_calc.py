import numpy as np
a = np.array([range(4),range(10,14)])
b = np.array([2,-1,1,0])
product_ab = a*b
print 'a=',a
print 'b=',b
print 'product_ab', product_ab

b1 = 100*b
print b1
b2 = b * 100.0
print b2

print b1==b2
print b1.dtype, b2.dtype
