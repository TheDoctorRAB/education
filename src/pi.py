#######
# Sample lecture problem
# Monte Carlo
# finding pi 
# rev.21.Aug.15
####### imports
import numpy
import random
#######
#
#
#
#######
print 'This is pi: ',numpy.pi
#######
N=int(raw_input('enter N: '))
radius=int(raw_input('enter radius: '))
#
x=0
y=0
r_sq=0
#
hit=0
sum=0
###
for i in range(0,N):
    x=random.uniform(0,radius)
    y=random.uniform(0,radius)
    r_sq=x**2+y**2
    if(r_sq**0.5<radius):
	hit=hit+1
# end
# end
sum=float(4)*float(hit)/float(N)
print numpy.pi,sum
########################################################################
#      EOF
########################################################################
