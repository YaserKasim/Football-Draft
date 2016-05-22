# edouard long 2015

# the main function that will read the text file
def readTextFile():

    # intialise an array the players will go into
    players = []

    # initiase a counter
    counter = -1

    # open the file
    file = open("playerDatabase.txt","r")

    # initialise a var that keeps track of whether we have read the whole file
    done = False

    # initilasie a loop that goes until we read the file
    while not done:
    
        # first read the next line
        line = file.readline().rstrip("\n")
        
        # check if there is a * and we need to create a new array
        if line == "*":

            # create a new array in the players
            players.append([])

            # incriment the counter
            counter += 1

        # check if the file has ended
        if line == "***":

            # close the file
            file.close()

            # break the loop
            done = True

        # else put the info into the array
        else:

            # add the info in
            players[counter].append(line)

    print(players)

readTextFile()
            
