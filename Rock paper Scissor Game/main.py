#Rock paper Scissor Game

import random
l=['rock','paper','scissor']


#rock Vs paper => paper wins
#rock Vs scissor => rock wins
#paper Vs scissor => scissor wins



while True:
    ccount=0
    ucount=0
    usercho=int(input('''
Game Start.....
1. Yes
2. No| Exit 
    '''))

    if usercho==1:
        for a in range(1,6):
            userInput=int(input('''
1.Rock
2.Scissor
3.Paper
            '''))
            if userInput==1:
                uchoice='rock'
            elif userInput==2:
                uchoice='scissor'
            elif userInput==3:
                uchoice='paper'
            Cchoice=random.choice(l)
            if Cchoice ==uchoice:
                print("Computer value:",Cchoice)
                print('User Choice: ',uchoice)
                print('Game Draw')
                ucount +=1
                ccount +=1
            elif (uchoice=='rock' and Cchoice=='scissor')or (uchoice=='paper' and Cchoice=='rock') or (uchoice=='scissor' and Cchoice=='paper'):
                print("Computer value:",Cchoice)
                print('User Choice: ',uchoice)
                print("You Win")
                ucount +=1
            else:
                print("Computer value:",Cchoice)
                print('User Choice: ',uchoice)
                print("Computer Win")
                ccount +=1
                
        if ucount == ccount:
            print('Final Game Draw....')
            print("User Score:",ucount)
            print("Computer Score",ccount)
        elif ucount>ccount:
            print("Final you win the game....")
            print("User Score:",ucount)
            print("Computer Score",ccount)
        elif ucount<ccount:
            print("Final Computer win the game....")
            print("User Score:",ucount)
            print("Computer Score",ccount)

    else:
        break