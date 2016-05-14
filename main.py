# Edouard Long 2015

# a function that will display the formation with all of the given players ( takes in a formation and the players )
def showSquad(formation, players):

    # first clear the screen
    print("\n" * 80)

    # print a title in the middle of the screen
    print("\n" * 5)

    # initialise a counter that keeps track of which player we are on
    counter = 0 

    # initialise a loop that will loop through each row of the formation and print out the rows inside it
    for row in formation:

        # print out 10 new lines ( dont if this is the fist row)
        if counter != 0:
            print("\n" * 10)

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


# create an array of 11 players
players = [["Player 1","striker","87"],["Player 2","striker","87"],["Player 3","mid","87"],["Player 4","mid","87"],["Player 5","mid","87"],["Player 6","mid","87"],["Player 7","mid","87"],["Player 8","mid","87"],["Player 9","def","87"],["Player 10","def","87"],["Player 11","gk","87"]]

# create a formation we will use
formation = [3,3,4,1]

# print out the squad
showSquad(formation,players)
    
