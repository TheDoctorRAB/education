#######
# Sample lecture problem
# Monte Carlo
# Brown, 1-6
# rev.27.Jul.15
####### imports
import numpy
import random
#######
#
#
#
#######
# mathematical approach
N=1000000
x=0
y=0
sum=0
#
for i in range(0,N):
    x=random.random()
    eval=(1-x**2)**(.5)    
    y=y+eval
# end
sum=y/N
print 'For ',N,': ',sum
#######
# simulation approach
hit=0
x=0
y=0
z=0
sum=0
#
for j in range(0,N):
    x=random.random()
    y=random.random()
    z=x**2+y**2
    if (z<=1):
	hit=hit+1
# end
# end
sum=float(hit)/float(N)
print 'For ',N,': ',sum
########################################################################
#      EOF
########################################################################
