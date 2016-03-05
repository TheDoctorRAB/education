########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.26.February.2016
########################################################################
#
# Risk assessment failure rate example 
#
########################################################################
#
# imports
#
import pandas
import numpy
from sys import argv
script,failure_csv=argv
#
########################################################################
#
#
#
#######
#
failure_dataset=numpy.loadtxt(failure_csv,dtype=int,delimiter='\t')
#
#######
#
failure_sort=pandas.DataFrame(failure_dataset)
#
#######
#
sorted_failures=failure_sort.sort([2,1],ascending=[False,True])
numpy.savetxt('sorted.data.out',sorted_failures,fmt='%i',delimiter='\t')
#
########################################################################
#
# EOF
#
########################################################################
