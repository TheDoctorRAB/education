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
total_equipment_tested=random.randint(250,750)
eta=random.randint(1000,4500)
beta=random.uniform(0.25,1.75)
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
    equipment_failure_data[i,0]=random.randint(0,999)  #hrs
    equipment_failure_data[i,1]=1-numpy.exp(-(equipment_failure_data[i,0]/eta)**beta) #Q(t)
# end i
#
#######
#
# write equipment failure data
#
numpy.savetxt('equipment.failure.simulation.data.out',equipment_failure_data,fmt='%i\t%.6f',header='hrs\tQ(t)')
#
########################################################################
#
# EOF
#
########################################################################
