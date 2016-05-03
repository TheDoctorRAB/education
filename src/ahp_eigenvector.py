########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.28.April.2016
# v1.0
########################################################################
#
# Read in a csv file n x n matrix.
# Matrix is reciprocal for AHP.
# Computes eigenvalues and eigenvectors.
# It looks like the real/max eigenvalue is listed first.
# Then, the associated vectors are the columns of the matrix.
#
########################################################################
#
# imports
#
import numpy
import scipy
from sys import argv
script,matrix_data=argv #add a CSV file with email addresses (one on each line) as command line argument
#
########################################################################
#
# read in the matrix
#
ahp_matrix=numpy.loadtxt(matrix_data,dtype=float)
ahp_index=len(ahp_matrix)
assoc_eigenvector=numpy.zeros(ahp_index)
normalized_eigenvector=numpy.zeros(ahp_index)
#
#######
#
# compute eigenvalues and eigenvectors
#
eigenvalues,eigenvectors=numpy.linalg.eig(ahp_matrix) #eigenvalues in one row array; eigenvectors in matrix
max_eigenvalue=numpy.real((numpy.amax(eigenvalues))) #maximum real eigenvalue is first
eigen_sum=0
for i in range(0,ahp_index):
   eigen_sum=eigen_sum+eigenvectors[i,0]
# end i
#
for j in range(0,ahp_index):
    assoc_eigenvector[j]=eigenvectors[j,0] #eigenvectors in columns
# end j
#
for k in range(0,ahp_index):
    normalized_eigenvector[k]=assoc_eigenvector[k]/eigen_sum	
# end k
#
#######
#
# consistency index
#
consistency_index=(max_eigenvalue-ahp_index)/(ahp_index-1)
#
#######
#
# output
#
print 'AHP matrix'
print ahp_matrix
print
print 'AHP matrix index: ',ahp_index 
print
print
print 'eigenvalues',eigenvalues
print
print
print 'maximum eigenvalue: ',max_eigenvalue 
print
print
print 'associated eigenvector' 
print assoc_eigenvector
print
print
print 'normalized eigenvector'
print normalized_eigenvector
print
print
print 'consistency index: ',consistency_index
#
ahp_data=open('ahp.out','w+')
ahp_data.write(str.format('AHP index')+'\t'+str.format('%i'%ahp_index)+'\n'+str.format('consistency index')+'\t'+str.format('%.6f'%consistency_index)+'\n'+str.format('maximum eigenvalue')+'\t'+str.format('%.6f'%max_eigenvalue)+'\n\n'+str.format('associated eigenvector')+'\n')
#
for m in range(0,ahp_index):
    ahp_data.write(str.format('%.6f'%assoc_eigenvector[m])+'\n')
# end m
#
ahp_data.write('\n'+str.format('normalized eigenvector')+'\n')
#
for n in range(0,ahp_index):
    ahp_data.write(str.format('%.6f'%normalized_eigenvector[n])+'\n')
# end n
ahp_data.close()
#
########################################################################
#
# EOF
#
########################################################################
