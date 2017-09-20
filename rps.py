import random

ltr=('s','r','p')

amt=50
wins=0
losses=0
ties=0

def printMoney():
	print('you have $' + str(amt))

playAgain=('y')

while (amt>=10) and (playAgain=='y'):
	printMoney()
	play=input('Choose r, p or s: ')
	myPlay=random.choice(ltr)
	if play==myPlay:
		print('computer chose: '+ str(myPlay))
		print('you tied with the computer!')
		amt=amt
		ties=ties+1
		print('-----------------------------')
		printMoney()
		print('wins: '+ str(wins))
		print('losses: '+ str(losses))
		print('ties: '+str(ties))
		print('-----------------------------')
		playAgain=input('play again? y or n ')
	elif play=='r':
		if myPlay=="p":
			print('computer chose: '+ str(myPlay))
			print('computer beat you')
			amt=amt-10
			losses=losses+1
			print('-----------------------------')
			printMoney()
			print('wins: '+ str(wins))
			print('losses: '+ str(losses))
			print('ties: '+str(ties))
			print('-----------------------------')
			playAgain=input('play again? y or n ')
		else:
			print('computer chose: '+ str(myPlay))
			print('you beat computer')	
			amt=amt+10
			wins=wins+1
			print('-----------------------------')
			printMoney()
			print('wins: '+ str(wins))
			print('losses: '+ str(losses))
			print('ties: '+str(ties))
			print('-----------------------------')
			playAgain=input('play again? y or n ')
	elif play=='p':
		if myPlay=="s":
			print('computer chose: '+ str(myPlay))
			print('computer beat you')
			amt=amt-10
			losses=losses+1
			print('-----------------------------')
			printMoney()
			print('wins: '+ str(wins))
			print('losses: '+ str(losses))
			print('ties: '+str(ties))
			print('-----------------------------')
			playAgain=input('play again? y or n ')
		else:
			print('computer chose '+ myPlay)
			print('you beat computer')	
			amt=amt+10
			wins=wins+1
			print('-----------------------------')
			printMoney()
			print('wins: '+ str(wins))
			print('losses: '+ str(losses))
			print('ties: '+str(ties))	
			print('-----------------------------')
			playAgain=input('play again? y or n ')
	elif play=='s':
		if myPlay=="r":
			print('computer chose '+ myPlay)
			print('computer beat you')
			amt=amt-10
			losses=losses+1
			print('-----------------------------')
			printMoney()
			print('wins: '+ str(wins))
			print('losses: '+ str(losses))
			print('ties: '+str(ties))
			print('-----------------------------')
			playAgain=input('play again? y or n ')
		else:
			print('computer chose '+ myPlay)
			print('you beat computer')	
			amt=amt+10
			wins=wins+1
			print('-----------------------------')
			printMoney()
			print('wins: '+ str(wins))
			print('losses: '+ str(losses))
			print('ties: '+str(ties))
			print('-----------------------------')
			playAgain=input('play again? y or n ')
	else:
		playAgain=input('play again? y or n ')

printMoney()

if amt<10:
	print('You do not have enough money! You are done.')
