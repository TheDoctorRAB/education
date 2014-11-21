########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.20.November.2014
########################################################################
# Russian roulette
########################################################################
#
########################################################################
# What is the probability of dying for a six player Russian roulette game?
# Six chamber gun, but the chamber is respun after every failed attempt.
# There should be a convergence if the routine is carried out to a sufficient number of rounds.
# If not, just increase the number of rounds. 
########################################################################
#
########################################################################
# While the analytical solution is not that difficult, this can also be simulated 'experimentally.'
######################################################################## 
#
#
#
####### imports
import numpy
######################################################################## 
#
#
#
####### function kill
# Since the gun is 'fair' the probability of the gun firing is always the same.
# If the gun goes off, the player dies. 
###
# chamber_size=6
####### Assign probabilities
#      Probability of the gun shooting
ps=float(1)/6
#      Probability of the gun not shooting
pns=1-ps
#######
#      
####### How many players?
number_of_players=6
player=[]
#######
#
####### How many rounds?
rounds=10
#######
#
####### Initialize players
for i in range (0,number_of_players):
       player.append(0)
# end i
#######
#
####### Calculate probability
for n in range(0,rounds):
       for i in range (0,number_of_players):
              player[i]=player[i]+(ps)*(pns)**(number_of_players*n+i)
              print n,i,player[i]
# end i
# end n
#######
#
#######
print 'final round',rounds
for i in range (0,number_of_players):
       print round(player[i],4)
# end i
#
#######
#      EOF
#######
