#######
# Sample lecture problem
# Monte Carlo
# finding square root of two 
# rev.21.Aug.15
####### imports
import numpy
import random
#######
#
#
#
#######
print 'This is the square root of two: ',numpy.sqrt(2)
#######
N=int(raw_input('enter N: '))
#
x=0
y=0
f_x=0
#
hit=0
sum=0
###
for i in range(0,N):
    x=random.uniform(0,1)
    y=random.uniform(0,1)
    f_x=x+y
    if(f_x<1):
	hit=hit+1
# end
# end
sum=(float(4)*((float(hit)/float(N))))**(0.5)
print numpy.sqrt(2),sum
########################################################################
#      EOF
########################################################################
