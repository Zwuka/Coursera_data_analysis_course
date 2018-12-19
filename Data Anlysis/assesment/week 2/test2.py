

#table = [(x,x*2) for x in range(2009,2011)]
#print (type(table[0]))

a = '2,12'

try:
    float(a)
except ValueError:
    a
    