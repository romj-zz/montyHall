from random import randint
import itertools

def playMontyHall(switchDoor) :
	#Number of doors :
	numberofDoors = 3
	verbose = 1
	if verbose :
		print "---------------- STARTING GAME ----------------"
	# We have 3 doors (0,1,2), with goats behind two of them and a car behind the other one :
	carPosition = randint(0,numberofDoors - 1)
	if verbose :
		print "carPosition = "+str(carPosition)
	# The player chooses one door :
	playerChoice = randint(0,numberofDoors - 1)
	if verbose :
		print "playerChoice = "+str(playerChoice)
	# Monty Hall shows one door that the player has not chosen and that is not the winning door :
	availableDoorsToOpen = []
	for door in range(numberofDoors):
		if door != carPosition and door != playerChoice:
			availableDoorsToOpen.append(door)
	openedDoor = availableDoorsToOpen[randint(0,len(availableDoorsToOpen)-1)]
	if verbose :
		print "openedDoor = "+str(openedDoor)
	# The player has an opportunity to change his choice
	if (switchDoor):
		availableDoorsToSwitch = range(numberofDoors)
		# His choice won't be the first one
		availableDoorsToSwitch.remove(playerChoice)
		# His choice won't be the opended door
		availableDoorsToSwitch.remove(openedDoor)
		playerChoice = availableDoorsToSwitch[randint(0,len(availableDoorsToSwitch)-1)]
		if verbose :
			print "switching, playerChoice = "+str(playerChoice)
	# We get the final result :
	if playerChoice == carPosition:
		if verbose :
			print "XXXXXXXXXXXXXXXX Win ! XXXXXXXXXXXXXXXX"
		return 1
	else:
		if verbose :
			print "XXXXXXXXXXXXXXXX Lose ! XXXXXXXXXXXXXXXX"
		return 0

numberOfTests = 10

wonBySwitching = 0
wonByNotSwitching = 0
for _ in itertools.repeat(None, numberOfTests):
    wonBySwitching = wonBySwitching + playMontyHall(1)
    wonByNotSwitching = wonByNotSwitching + playMontyHall(0)

winProbaOfSwitching = wonBySwitching*100/numberOfTests
winProbaOfNotSwitching = wonByNotSwitching*100/numberOfTests

print "wonBySwitching = "+str(wonBySwitching)+", ie a probability of "+str(winProbaOfSwitching)+"% of winning"
print "wonByNotSwitching = "+str(wonByNotSwitching)+", ie a probability of "+str(winProbaOfNotSwitching)+"% of winning"
