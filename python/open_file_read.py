with open('/Work/Scripts_codes/python/ncas-isc/python/exercises/example_data/weather.csv','r') as padhle:
    data = padhle.read()
    print data
    print len(data)
    total = 0
    count = 1
    line = data
    line = padhle.readline()

    while line !='':
       count = count + 1
       total = total + len(line)
       line = padhle.readline(11)
       print line
