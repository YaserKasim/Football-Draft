# Edouard Long 2015
import random

# a function that will display the formation with all of the given players ( takes in a formation and the players )
def showSquad(formation,players,subs,manager):

    # first clear the screen
    print("\n" * 80)

    # first print out the manager
    print("Manager:\n")
    print(manager[0].capitalize())

    # print a title in the middle of the screen
    print("\n" * 3)

    # initialise a counter that keeps track of which player we are on
    counter = 0 

    # initialise a loop that will loop through each row of the formation and print out the rows inside it
    for row in formation:

        # print out 10 new lines ( dont if this is the fist row)
        if counter != 0:
            print("\n" * 9)

        # initialse a new string that contains the whole of each row
        contentsOfRow = ""

        # if there are only 1,2 or 3 players, add some white space to make the list appear in the middle
        if row == 1:
            contentsOfRow += "                                                              "
        elif row == 2:
            contentsOfRow += "                                                  "
        elif row == 3:
            contentsOfRow += "                                     "
        elif row == 4:
            contentsOfRow += "                        "

        # initialise a loop that goes through the len of each row
        for player in range(0, row):

            # add some white space to the string
            contentsOfRow = contentsOfRow + "      "

            # add the player's name to the string
            contentsOfRow += players[counter][0].capitalize() + "    "

            # add the players position to the string
            contentsOfRow += players[counter][1].upper()+ "    "

            #move onto the next player
            counter += 1

        # print out the row
        print(contentsOfRow)

    # print out the subs
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nSubs:\n")

    # initialise the row that contians the subs
    contentsOfRowSubs = ""

    # initialse a counter
    counter = 0

    # initialse a new string that contains the whole of each row
    contentsOfRowSubs = ""

    # loop through all the subs and print them out
    for sub in subs:

        # add some white space to the string except if it is first sub
        if counter != 0 :
            contentsOfRowSubs = contentsOfRowSubs + "    "

        # add the subs's name to the string
        contentsOfRowSubs += subs[counter][0].capitalize() + "    "

        # add the subs position to the string
        contentsOfRowSubs += subs[counter][1].upper()+ "    "

        #move onto the next player
        counter += 1

    # print the subs
    print(contentsOfRowSubs)

        
    
# create a main func
def main(formationToUse):

    # create the manager
    manager = ["Player 0","2"]

    # create an array of 11 players
    players = [["Player 1","pos","50"],["Player 2","pos","50"],["Player 3","pos","50"],["Player 4","pos","50"],["Player 5","pos","50"],["Player 6","pos","50"],["Player 7","pos","50"],["Player 8","pos","50"],["Player 9","pos","50"],["Player 10","pos","50"],["Player 11","pos","50"]]

    # create an array of 5 subs
    subs = [["Player 12","pos","50"],["Player 13","pos","50"],["Player 14","pos","50"],["Player 15","pos","50"],["Player 16","pos","50"]]

    # create a formation we will use
    formation = formationToUse

    # get that formation in numbers
    formationInNumbers = []

    # loop through the formation
    for row in reversed(formation):

        # get the len of that array
        formationInNumbers.append(len(row))

    # print out the squad
    showSquad(formationInNumbers,players,subs,manager)

    # print some dashes
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    
    # first, determine if the user wants to swap a sub with a player or get new players for a position
    userChoice = input("If you want to get new players for a position type 'players' or if you want to swap a sub with a player type 'swap'\n")

    # see which one the user typed in
    if userChoice == 'swap':

        # first, get which sub the user wants to swap
        subToSwap = int(input("Please type which sub you want to swap (For first sub type '1')\n")) - 1

        # next, get the player number which the user wants to swap the sub with
        playerToSwap = int(input("Please type in the player that you want to swap the sub with (type their number)\n")) - 1

        # store the sub in a value
        subInfo = subs[subToSwap]

        # remove the sub from this array
        subs.pop(subToSwap)

        #store the player in a value
        playerInfo = players[playerToSwap]

        # remove the player
        players.pop(playerToSwap)

        # put the sub where the player was
        players.insert(playerToSwap,subInfo)

        # put the player where the sub was
        subs.insert(subToSwap,playerInfo)

        showSquad(formationInNumbers,players,subs,manager)
        

    else:
    
        # get the user to choose a number
        userInput = int(input("Please choose a player to get positions for (type in their number)\n"))

        # create a reversed formation of the array
        reversedFormation = formation[::-1]
        
        # check if the user has chosen a sub
        if userInput > 11:
            userRow = len(reversedFormation) + 1

        # check if the user has chosen the manager
        elif userInput == 0:
            userRow = 0

        # else find the row of the player they chose
        else:
            # initialise a currentrow value
            currentRow = 0

            # initialise the users row
            userRow = 0

            # determine which row the user's player is on
            for row in range(0,len(reversedFormation) + 1):
                
                # get the number of players in the next row
                currentRow = currentRow + len(reversedFormation[row])
                        
                # check if the player is in this row
                if (currentRow - userInput) >= 0:

                    # the user has chosen this row
                    userRow = row + 1
                    
                    break

        print("The row you have chosen is " + str(userRow))
        
        # find the position of that player if it is not a sub
        if userRow != 0 and userRow < len(reversedFormation) + 1:
            
            # first find out how many rows are before the player and add it to a var
            totalOfRowsBefore = 0
            for row in range(0,userRow - 1):

                # get the total of the rows before
                totalOfRowsBefore += len(reversedFormation[row])

            # set the positon of the player equal to the totalofrowsbefore minus the user's input
            playerPosition = reversedFormation[userRow-1][userInput - totalOfRowsBefore - 1]

        # check if a sub was chosen
        elif userRow == len(reversedFormation) + 1:

            # set the player position to 'sub'
            playerPosition = 'sub'

        # check if a manager was chosen
        elif userRow == 0:

            # set the player pos to 'manager'
            playerPosition = 'manager'

        print("The position of your player is: " + playerPosition.upper())


def pickFormation():
    formation = []
    random1 = random.randint(0,len(formation))
    formation.append([['gk'],['cb','cb','cb'],['lm','cm','cm','rm'],['cam'],['st','st']])
    formation.append([['gk'],['cb','cb','cb'],['lm','cm','cm','rm'],['lf','rf'],['st']])
    formation.append([['gk'],['cb','cb','cb'],['lm','cm','cm','rm'],['lf','st','rf']])
    formation.append([['gk'],['cb','cb','cb'],['lm','cdm','cdm','cam','rm'],['st','st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cdm'],['lm','rm'],['cam'],['st','st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cdm'],['lm','cm','cm','rm'],['st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cdm','cdm'],['cam'],['cam','cam'],['st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cdm','cdm',],['cam','cam'],['st','st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cdm'],['lm','cm','cm','rm'],['st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cm','cm','cm'],['cam'],['st','st']])
    formation.append([['gk'],['lb','cb','cb','rb'],['cm','cm','cm'],['lf','rf'],['st']])

    numberOfFormations = 5
    listOfRandomItems = random.sample(formation,numberOfFormations)

    letters = ["A: ","B: ","C: ","D: ","E: "]

    counter = 0
    
    for formation in listOfRandomItems:
        strToPrint = []
        for row in formation [1:]:
             strToPrint.append(len(row))
        
        print(letters[counter],strToPrint)

        counter += 1

    userChoice = input('\nWhich formation do you want? A, B, C, D or E?\n').upper()
    if userChoice == 'A' :
        main(listOfRandomItems[0])
    if userChoice == 'B':
        main(listOfRandomItems[1])
    if userChoice == 'C':
        main(listOfRandomItems[2])
    if userChoice == 'D':
        main(listOfRandomItems[3])
    if userChoice == 'E':
        main(listOfRandomItems[4])

pickFormation()

        

    

    
    
