#######
# Sample lecture problem
# Chapter 3, page 107, #89
####### imports
import numpy
import matplotlib.pyplot as plot
from matplotlib.ticker import MultipleLocator
#######
temperature=numpy.zeros((100,2))
###
j=0
for i in range(0,100):
  temperature[i,0]=j
  temperature[i,1]=((4*j*j)/(j+2))-20
  j=j+0.1
# end i
print temperature
###
#
####### plot the sorted z scores
# set up for two y axis
fig,pdf_axis=plot.subplots()
###
# text
plot.title('Refrigeration plant testing')
pdf_axis.set_xlabel('time [h]')
pdf_axis.set_ylabel('Temperature [C]')
###
# axis
plot.xlim(0,10)
pdf_axis.axis(ymin=-20,ymax=10)
pdf_axis.xaxis.set_major_locator(MultipleLocator(1))
pdf_axis.xaxis.set_minor_locator(MultipleLocator(0.25))
pdf_axis.yaxis.set_major_locator(MultipleLocator(5))
pdf_axis.yaxis.set_minor_locator(MultipleLocator(1))
pdf_axis.tick_params(axis='both',which='major',direction='inout',length=7)
###
# grid
pdf_axis.grid(which='major',axis='both',linewidth='1.1')
pdf_axis.grid(which='minor',axis='x')
###
# plot
pdf_axis.plot(temperature[:,0],temperature[:,1])
plot.show()
###
# save
# this is not currently working for some reason
###
plot.savefig('refrigeration')
#######
#
####### write file
numpy.savetxt('temperature.out',temperature)
#######
#
#
########################################################################
#      EOF
########################################################################
