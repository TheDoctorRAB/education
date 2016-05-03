########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.26.February.2016
########################################################################
#
# Generates random failure data for a hypothetical equipment.
# Use for TM529 HW5.
#
########################################################################
#
# imports
#
import numpy
import random
from scipy.stats import expon
#
########################################################################
#
#
#
#######
#
# total pieces of equipment tested
#
total_equipment_tested=random.randint(250,750)
beta=random.randint(1000,4500)
#
#######
#
# initialze data matrix
#
equipment_failure_data=numpy.zeros((total_equipment_tested,2))
#
# generate failure data
#
for i in range(0,total_equipment_tested):
    equipment_failure_data[i,0]=random.randint(0,999)  #equipment ID
    equipment_failure_data[i,1]=numpy.random.exponential(beta) #failure time
#    x=random.random()
#    y=expon.cdf(equipment_failure_data[i,1],scale=beta)
#    if(x>y):
#	equipment_failure_data[i,2]=0
#    else:
#	equipment_failure_data[i,2]=1
# end if
# end i
#
#######
#
# write equipment failure data
#
numpy.savetxt('equipment.failure.data.out',equipment_failure_data,fmt='%03d\t%i',header='ID\thrs')
#
########################################################################
#
# EOF
#
########################################################################
