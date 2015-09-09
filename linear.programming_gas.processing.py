#######
# Sample lecture problem
# Linear programming
# NE225 week 8
# rev.08.Sep.15
# @TheDoctorRAB
#######
# 
# A gas processing plant receives a fixed amount of raw gas each week.
# Either regular or premium quality is processed, but only one grade at a time.
# The plant is open 80 hours per week.
#
# Decision variables are quantity of regular gas produced per week and premium gas produced each week.
# 
# Objective function is to maximize profit under given constraints.
#
#######
#
#
#
####### imports
import numpy
import matplotlib.pyplot as plot
from matplotlib.ticker import MultipleLocator
import pylab
#######
#
#
#
####### decision variables
regular_gas_volplot=numpy.zeros(100)
premium_gas_volplot=numpy.zeros(100)
#
regular_gas_productionplot=numpy.zeros(100)
premium_gas_productionplot=numpy.zeros(100)
#
regular_gas_storageplot=numpy.zeros((100,2))
premium_gas_storageplot=numpy.zeros((100,2))
#######
#
#
#
####### constraints
regular_gas_volume=7 #cubic meters/ton
premium_gas_volume=11 #cubic meters/ton
volume_constraint=77 #cubic meters/week
#
regular_gas_production_time=10 #hours/ton
premium_gas_production_time=8 #hours/ton
production_time=80 #hours/week
#
regular_gas_storage=9 #ton
premium_gas_storage=6 #ton
#######
#
#
#
####### objective function
regular_gas_profit=150 #$/ton
premium_gas_profit=175 #$/ton
#######
#
#
#
####### graph constraints 
#
# premium_gas (y axis) v regular_gas (x axis)
#
### volume constraint
j=0
for i in range(0,100):
    regular_gas_volplot[i]=j
    regular_gas_productionplot[i]=j
    regular_gas_storageplot[i,1]=j
    premium_gas_storageplot[i,0]=j
#
    premium_gas_volplot[i]=(float(volume_constraint)/float(premium_gas_volume))-(float(regular_gas_volume)/float(premium_gas_volume))*regular_gas_volplot[i]
    premium_gas_productionplot[i]=(float(production_time)/float(premium_gas_production_time))-(float(regular_gas_production_time)/float(premium_gas_production_time))*regular_gas_productionplot[i]
    regular_gas_storageplot[i,0]=regular_gas_storage
    premium_gas_storageplot[i,1]=premium_gas_storage
#
    j=j+1
# end
#######
#
#
#######
# set up for two y axis
fig,left_axis=plot.subplots()
#right_axis=left_axis.twinx()
###
# plot text
title='Gas processing example' 
xtitle='Regular gas produced [ton/week]'
ytitle='Premium gas produced [ton/week]'
line_color1='Blue'
line_color2='Red'
line_color3='Black'
line_color4='Green'
###
plot.title(title,fontsize=18)
left_axis.set_xlabel(xtitle,fontsize=16)
left_axis.set_ylabel(ytitle,fontsize=16)
#right_axis.set_ylabel()
###
# axis
xmin=0
xmax=15
#
ymin=0
ymax=15
#
xmajortick=1
ymajortick=1
#
xminortick=0.25
yminortick=0.25
###
plot.xlim(xmin,xmax)
left_axis.axis(ymin=ymin,ymax=ymax)
#
left_axis.xaxis.set_major_locator(MultipleLocator(xmajortick))
left_axis.xaxis.set_minor_locator(MultipleLocator(xminortick))
left_axis.yaxis.set_major_locator(MultipleLocator(ymajortick))
left_axis.yaxis.set_minor_locator(MultipleLocator(yminortick))
#
left_axis.tick_params(axis='both',which='major',direction='inout',length=7)
###
# grid
left_axis.grid(which='major',axis='both',linewidth='1.1')
#       left_axis.grid(which='minor',axis='both')
###
# plot
left_axis.plot(regular_gas_volplot,premium_gas_volplot,color=line_color1,label='Volume constraint: 7r+11p=77')
left_axis.plot(regular_gas_productionplot,premium_gas_productionplot,color=line_color2,label='Production constraint: 10r+8p=80')
left_axis.plot(regular_gas_storageplot[:,0],regular_gas_storageplot[:,1],color=line_color3,label='Regular gas storage: r=9')
left_axis.plot(premium_gas_storageplot[:,0],premium_gas_storageplot[:,1],color=line_color4,label='Premium gas storage: p=6')
###
pylab.legend(loc='upper right')
plot.get_current_fig_manager().resize(1920,1080)
plot.show()
###
# save
plot.savefig(title)
#######
#
########################################################################
#      EOF
########################################################################
