import numpy as np
x = range(1,11)
a1 = np.array(x,np.int32)
a2 = np.array(x,np.float32)
print x[0:8]
print 'a1 data type is', a1.dtype
print 'a2 data type is', a2.dtype
