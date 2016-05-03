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
#########################################################################
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
# In other words it is a random sample from a uniform distribution.
# If the gun goes off, the player dies. 
###
# size of the chamber determines the probability of the gun firing
chamber_size=6
###
def gunfire(chamber_size): 
###
#
### initialize kill count
    kill=0
###
#
### fire the gun
    fire=numpy.random.random_integers(0,chamber_size-1)
###
#
### determine if the gun fired
    if (fire==0):
	kill=1
# end if
###
    return(kill)
########################################################################
#
#
#
####### initialize players, kills, attempts
number_of_players=6
player_attempts=numpy.zeros((number_of_players))
player_kills=numpy.zeros((number_of_players))
player_probability=numpy.zeros((number_of_players))
#######
#
#
#
####### main loop
#
# kill=0
for j in range(0,2): # number of times to run the game for the statistical base
    kill=0
    print 'game: ',j+1,'\n\n' 
    while(kill==0): # current game continues if all players survive 
	for i in range(0,number_of_players):
	    print 'player: ',i+1 
	    player_attempts[i]=player_attempts[i]+1
	    kill=gunfire(chamber_size)
	    print kill
	    if (kill==1):
		player_kills[i]=player_kills[i]+1
		print 'kill',
		print 'game over','\n\n'
		break
	    else:
		print 'survive',
		print 'continue','\n'
#######
# the problem is that the current game doesn't continue if all players don't die
#
#
####### postprocessing
print player_attempts,player_kills
###
for k in range(0,number_of_players):
    player_probability[k]=player_kills[k]/player_attempts[k]
# end k
###
print player_probability
#######
#
#
#
########################################################################
# EOF
########################################################################
