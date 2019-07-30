def main():
    ### OPTIONAL FUNCTION ###
    cleanFile()  # purpose stated in function definition
    #########################
    restaurants = {}  # create empty dictionary
    loadRestaurants(restaurants)
    printRestaurants(restaurants)
    ccQuery(restaurants)
    threeStarUp(restaurants)
    printRatings(restaurants)
    reservation(restaurants)
    foodType(restaurants, "health")
    foodType(restaurants, "chinese")
    foodType(restaurants, "seafood")


# Function definitions
def loadRestaurants(aDict):
    # open info file
    infile = open("lab6.dat", "r")
    # Local variables
    name = ''
    foodType = ''  # strings
    reserv = False  # boolean value
    rating = 0  # integer
    ccard = False  # boolean value
    line = ''  # empty string for line var
    # starting file reading
    line = infile.readline()  # processing of this variable will happen in while loop
    print(line)
    while line != "":  # loop until eof
        line = line.rstrip("\n").split(":")
        # line has 5 indexes: [ name, foodtype, reservations, ratings, credcard ]
        name = line[0]
        foodType = line[1]
        # convert line[2] to a boolean value for reserv
        if line[2].upper() == "YES":
            reserv = True
        # cast the rating(line[3]) into an integer value
        rating = int(line[3])
        # convert line[4] to a boolean value for ccard
        if line[4].upper() == "YES":
            ccard = True
        # Add all of this to restaurants dictionary
        # dictionary_name[ key ] = value
        aDict[name] = [foodType, reserv, rating, ccard]  # 4 indexes
        # reset boolean values
        reserv = ccard = False
        # Get next line
        line = infile.readline()
    # closing file
    infile.close()


def printRestaurants(aDict):
    for rest in aDict:
        print(rest, aDict[rest])


def ccQuery(aDict):
    # print the keys of the dictionary
    print(write(("&" * 80)))
    for key in aDict:
        print(key)
    print(write("&"*50))

    # Find all restaurants that accept credit cards
    print(write(("*" * 80)))
    print(write("*"))
    print(write("* Here are all the restaurants that accept Credit Cards:"))
    # Ccard boolean value is in last index.
    index = 3
    # for loop to loop through dictionary
    for key in aDict:
        # test for boolean val ==> aDict[ key ] [ value_index ]
        if aDict[key][index]:
            print(write("*\t%s" % key))
    print(write("*"))
    print(write(("*" * 80)))


def threeStarUp(aDict):
    # This function will look for restaurants that have three stars or more
    print(write(("*" * 80)))
    print(write("*"))
    print(write("* The following restaurants have 3 or more stars:"))
    # ratings were kept in the value list at index 2
    index = 2
    rating = 3
    # loop through dictionary ==> aDict[ key ] [ index ] >= 3
    for key in aDict:
        if aDict[key][index] >= rating:
            print(write("*\t%s" % key))
    print(write("*"))
    print(write(("*" * 80)))


def printRatings(aDict):
    # This function prints all the restaurants from the dictionary
    # in groups, according to their star rating. Decending order
    # local variables
    # index for rating is still 2
    index = 2
    maxStar = 5
    stop = 0
    print(write(("*" * 80)))
    print(write("*"))
    print(write("* Here are the restaurants listed by their ratings:"))
    for rating in range(maxStar, stop, -1):  # go from 5 to 1
        print(write("*\tHere are the restaurants with %s star(s):" % str(rating)))
        # Loop through dictionary
        for key in aDict:
            if aDict[key][index] == rating:
                print(write("*\t  %s" % key))
        print(write("*"))
    print(write(("*" * 80)))


def foodType(aDict, food):
    # This function will find all restaurants that have a certain type of food
    # food type is the first index in the value list
    # local variables
    index = 0
    print(write(("*" * 80)))
    print(write("*"))
    print(write("* The following restaurants serve %s food:" % food))
    for key in aDict:
        if aDict[key][index].lower() == food:
            print(write("*\t%s" % key))
    print(write("*"))
    print(write(("*" * 80)))


def reservation(aDict):
    # This function will list all the restaurants that accept reservations
    # reservation is located in the second index, or index = 1
    index = 1
    print(write(("*" * 80)))
    print(write("*"))
    print(write("* The following restaurants accept reservations:"))
    for key in aDict:
        if aDict[key][index]:  # boolean value
            print(write("*\t%s" % key))
    print(write("*"))
    print(write(("*" * 80)))


def write(string):
    # This function will be used inside all the print statements.
    # Hopefully it will save the string, write it to a file, and
    # then send the string back out to the print statement.
    # open file
    outfile = open("lab6.out", "a")
    # append should save me from having to have an out file open
    # for the entire duration of the program.
    outfile.write(string + "\n")
    outfile.close()
    return string


def cleanFile():
    '''
    The purpose of this function is to erase the contents of
    the input  file so that you can run the program multiple
    times, and not have the data saved from each iteration.
    If you would like to keep the output from each run,
    then you just comment out the function call.
    '''
    file = open("lab6.out", "w")
    file.close()


# Call main
main()