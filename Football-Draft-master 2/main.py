# Edouard Long 2015

# a function that will display the formation with all of the given players ( takes in a formation and the players )
def showSquad(formation,players,subs,manager):

    # first clear the screen
    print("\n" * 80)

    

    # first print out the manager
    print("Manager:\n")
    print(manager[0].capitalize() + "      " + manager[1].upper())

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
            contentsOfRow += "                                         "
        elif row == 3:
            contentsOfRow += "                               "
        elif row == 4:
            contentsOfRow += "               "

        # initialise a loop that goes through the len of each row
        for player in range(0, row):

            # add some white space to the string
            contentsOfRow = contentsOfRow + "      "

            # add the player's name to the string
            contentsOfRow += players[counter][0].capitalize() + "    "

            # add the players position to the string
            contentsOfRow += players[counter][1].upper()+ "    "

            # add the player's rating to the string
            contentsOfRow += players[counter][2]+ "    "

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

        # add the subs's rating to the string
        contentsOfRowSubs += subs[counter][2]+ "    "

        #move onto the next player
        counter += 1

    # print the subs
    print(contentsOfRowSubs)

        
    
# create a main func
def main():

    # create the manager
    manager = ["Player 0","4"]

    # create an array of 11 players
    players = [["Player 1","striker","87"],["Player 2","striker","87"],["Player 3","mid","87"],["Player 4","mid","87"],["Player 5","mid","87"],["Player 6","mid","87"],["Player 7","mid","87"],["Player 8","mid","87"],["Player 9","def","87"],["Player 10","def","87"],["Player 11","gk","87"]]

    # create an array of 5 subs
    subs = [["Player 12","striker","87"],["Player 13","DEF","87"],["Player 14","GK","87"],["Player 15","LW","87"],["Player 16","RW","87"]]

    # create a formation we will use
    formation = [['gk'],['lb','cb','cb','rb'],['rm','cm','lm'],['st','st','st']]

    # get that formation in numbers
    formationInNumbers = []

    # loop through the formation
    for row in reversed(formation):

        # get the len of that array
        formationInNumbers.append(len(row))

    # print out the squad
    showSquad(formationInNumbers,players,subs,manager)

    # print some dashes
    print("\n----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nSubs:\n")

    print("\n\n")
    
    # get the user to choose a number
    userInput = int(input("Please choose a player to swap (type in their number)\n"))
    
    # check if the user has chosen a sub
    if userInput > 11:
        userRow = len(formation) + 1

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
        for row in range(0,len(formation)):

            # get the number of players in the next row
            currentRow = currentRow + formation[row]
                    
            # check if the player is in this row
            if (currentRow - userInput) >= 0:

                # the user has chosen this row
                userRow = row + 1
                
                break

    print("The row you have chosen is " + str(userRow))


main()

        

    

    
    
