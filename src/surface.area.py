####### imports
import numpy
import matplotlib.pyplot as plot
from matplotlib.ticker import MultipleLocator
#######
radius=numpy.zeros((250,2))
###
j=5
surface_area=float(100000)
# compute z score
for i in range(0,250):
    radius[i,0]=j
    radius[i,1]=((-2*3.14*j)+((2*3.14*j)**2+(8*3.14*surface_area))**(0.5))/(4*3.14)
    j=j+5
# end i
print radius 
###
#
####### plot the sorted z scores
fig,pdf_axis=plot.subplots()
###
# text
plot.title('Cylindrical surface area dimensions 100000 sq meters')
pdf_axis.set_xlabel('radius [m]')
pdf_axis.set_ylabel('height [m]')
###
# axis
plot.xlim(0,1250)
pdf_axis.axis(ymin=10,ymax=150)
pdf_axis.xaxis.set_major_locator(MultipleLocator(50))
#pdf_axis.xaxis.set_minor_locator(MultipleLocator(0.25))
pdf_axis.yaxis.set_major_locator(MultipleLocator(50))
#pdf_axis.yaxis.set_minor_locator(MultipleLocator(1))
pdf_axis.tick_params(axis='both',which='major',direction='inout',length=7)
###
# grid
pdf_axis.grid(which='major',axis='both',linewidth='1.1')
pdf_axis.grid(which='minor',axis='x')
###
# plot
pdf_axis.plot(radius[:,0],radius[:,1])
plot.show()
###
# save
# this is not currently working for some reason
###
#plot.savefig('refrigeration')
#######
#
####### write file
numpy.savetxt('radius.out',radius)
#######
#
#
########################################################################
#      EOF
########################################################################
