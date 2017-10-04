
expense =  int(raw_input('hi say your monthly expense : '))

emi =  int(raw_input('Cool! what abt monthly emi : '))

loan =  int(raw_input('monthly loan : '))

total_gap =  int(raw_input('total gap expected : '))
highgap = expense + emi + loan + total_gap
print "gap is = ", highgap

nm =  str(raw_input('hi say ur name : '))
names = ['smita', 'aditya', 'panda']
for n in names:
	if n == nm:
	   print 'found your ename'
	   exit()
print 'not found'
nm1 =  str(raw_input('add ur name : '))
names.append(nm1)

nm =  str(raw_input('enter name now to confirm : '))

for n in names:
	if n == nm:
	   print 'found your ename'
	   exit()
print 'not found'	
