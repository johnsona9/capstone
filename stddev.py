import statistics
f = open('rainbow.txt', 'r')
line = f.read()
line = line.rstrip()
line = line.replace(' ', '')
a = line.split(',')
for x in range(0, len(a)):
    a[x] = float(a[x])
print len(a)
print statistics.mean(a)
print statistics.stdev(a)
f.close()
