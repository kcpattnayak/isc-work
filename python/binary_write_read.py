import struct
bin_data = struct.pack('bbbb',123,12,45,34)
with open('mybinary.dat','wb') as bwriter:
   bwriter.write(bin_data)
with open('mybinary.dat','rb') as breader:
   bdata = breader.read()
   data = struct.unpack('bbbb',bdata)
print data
