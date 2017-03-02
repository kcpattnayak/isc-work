with open('/Work/Scripts_codes/python/ncas-isc/python/exercises/example_data/weather.csv','r') as reader:
   header = reader.readline()
   rain = []
   for line in reader.readlines():
      r = line.strip().split(',')[-1]
      r = float(r)
      rain.append(r)
      
print rain

with open('myrain.txt','w') as writer:
   writer.write('rain\n')
   for r in rain:
       writer.write(str(r)+'\n')
