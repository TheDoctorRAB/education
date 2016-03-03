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
#
########################################################################
#
#
#
#######
#
# total pieces of equipment tested
#
total_equipment_tested=random.randint(100,500) 
#
#######
#
# initialze data matrix
#
equipment_failure_data=numpy.zeros((total_equipment_tested,3))
#
# generate failure data
#
for i in range(0,total_equipment_tested):
    equipment_failure_data[i,0]=random.randint(0,499)  #equipment ID
    equipment_failure_data[i,1]=random.randint(0,4500) #operating hours
    if (equipment_failure_data[i,1]<=100) or (equipment_failure_data[i,1]>=4100): #failure determination
	equipment_failure_data[i,2]=0
    else:
	equipment_failure_data[i,2]=random.randint(0,1)
# end if
# end i
#
#######
#
# write equipment failure data
#
numpy.savetxt('equipment.failure.data.csv',equipment_failure_data,fmt='%03d\t%i\t%i',header='ID\thrs\tF')
#
########################################################################
#
# EOF
#
########################################################################
