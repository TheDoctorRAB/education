########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.18.May.2014
########################################################################
# This script computes z scores for course grading and plots the results.
# An input file with the raw scores in the second column is required.
# I used the student IDs as 'markers' for the z scores.
# The maximum score needs to be input at max_score below.
# The class average and std is computed for the raw scores and the z scores.
# Then they are sorted.
# Two plots are produced. 
# (1) A scatter plot of ID v z score.
# (2) A line plot of pdf v z score.
# Normally, student scores follow a normal distribution.
# The average and std for the z scores should be 0 and 1.
# The pdf plot (2) is plotted to show that the scores follow the normal distribution.
# As a visual check, a theoretical distribution is calculated and can be plotted.
# This is also on the same plot as (1) and (2). 
########################################################################
#
#
####### imports
import numpy
import matplotlib.pyplot as plot
from matplotlib.ticker import MultipleLocator
from random import randint
from sys import argv
from scipy import stats
script,mcnpx_output=argv
#######
#
####### open data file
# column 1 is ID and column 2 is score
raw_score=numpy.loadtxt('engin110_raw.scores.inp')
#######
#
####### maximum score
max_score=1000
#######
#
####### normalize the raw scores
#
# compute class statistics
class_average=raw_score[:,1].mean()
class_std=raw_score[:,1].std(ddof=1)
print class_average,class_std
###
# initialize counter to count the number of students
i=0
###
# loop through to count the students
for line in raw_score:
  i=i+1
  class_size=i
# end line
###
# intialize the z score matrix
z_score=numpy.zeros((class_size,3))
###
# compute z score
for i in range(0,class_size):
  z_score[i,0]=raw_score[i,0].astype(int)
  z_score[i,1]=(raw_score[i,1]-class_average)/class_std
  z_score[i,2]=stats.norm.pdf(z_score[i,1], loc=0.0, scale=1.0)
# end i
###
# verify statistics
z_score_average=z_score[:,1].mean()
z_score_std=z_score[:,1].std(ddof=1)
print z_score_average,z_score_std
###
# sort data by z_score
sorted_z_score=z_score[z_score[:,1].argsort()]
#######
#
####### theoretical distribution
# with enough students, the grades would be a standard normal distribution
# this can compare the actual distribution to a standard normal
###
# initialize matrix
theoretical_z_score=numpy.zeros((10000,3))
###
# randomize
for i in range(0,9999):
    theoretical_z_score[i,0]=randint(1,max_score)
# end i
###
# compute theoretical statistics
theoretical_average=theoretical_z_score[:,0].mean()
theoretical_std=theoretical_z_score[:,0].std(ddof=1)
###
# compute z scores
for i in range(0,9999):
  theoretical_z_score[i,1]=(theoretical_z_score[i,0]-theoretical_average)/theoretical_std
  theoretical_z_score[i,2]=stats.norm.pdf(theoretical_z_score[i,1], loc=0.0, scale=1.0)
# end i
###
# sort dats by z score
sorted_theoretical_z_score=theoretical_z_score[theoretical_z_score[:,1].argsort()]
#######
#
####### plot the sorted z scores
# set up for two y axis
fig,pdf_axis=plot.subplots()
id_axis=pdf_axis.twinx()
###
#text
plot.title('ENGIN110 Spring 2014')
pdf_axis.set_xlabel('z score')
pdf_axis.set_ylabel('PDF')
id_axis.set_ylabel('ID')
###
# axis
plot.xlim(-3,3)
pdf_axis.axis(ymin=0,ymax=0.42)
pdf_axis.xaxis.set_major_locator(MultipleLocator(0.20))
pdf_axis.xaxis.set_minor_locator(MultipleLocator(0.04))
pdf_axis.yaxis.set_minor_locator(MultipleLocator(0.01))
pdf_axis.tick_params(axis='both',which='major',direction='inout',length=7)
###
# grid
pdf_axis.grid(which='major',axis='both',linewidth='1.1')
pdf_axis.grid(which='minor',axis='x')
###
# plot
pdf_axis.plot(sorted_z_score[:,1],sorted_z_score[:,2])
####
# turn this on to graphically confirm actual distribution is standard normal
#pdf_axis.plot(sorted_theoretical_z_score[:,1],sorted_theoretical_z_score[:,2],color='red')
###
id_axis.plot(sorted_z_score[:,1],sorted_z_score[:,0],linestyle="",marker="o",color='black')
plot.show()
###
# save
plot.savefig('engin110_normalized.scores.jpg')
#######
#
####### write file
numpy.savetxt('z_score.out',sorted_z_score)
#######
#
#
########################################################################
#      EOF
########################################################################
