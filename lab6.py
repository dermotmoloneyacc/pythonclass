# program to use structure
# list of different types
# author djmoloney
# acc summer 2019
# lab6.py
# prof onabajo

# global variable
N = 10


def main():
    # file declaration
    infile = open("lab6data.txt", "r")
    outfile = open("lab6.out", "w")
    # structure declaration
    restname = [""] * 10
    foodtype = [""] * 10
    reservation = [0] * 10
    rating = [0] * 10
    creditcards = [0] * 10
    # call functions
    loadx(infile, restname, foodtype, reservation, rating, creditcards)
    # query
    creditcard(outfile, restname, creditcards)
    stars(outfile, restname, rating)
    chinese(outfile, restname, foodtype, rating)
    ratings(outfile, restname, rating)
    health(outfile, restname, foodtype)
    # closefiles
    infile.close()
    outfile.close()


# functions
def loadx(file, A, B, C, D, E):
    # local variables
    K = 0
    while (K < N):
        templist = file.readline().strip("\n").split(",")
        #print(templist)
        A[K] = templist[0]
        B[K] = templist[1]
        C[K] = int(templist[2])
        D[K] = int(templist[3])
        E[K] = int(templist[4])
        K = K + 1


def creditcard(file, A, B):
    # local variable
    K = 0
    print("Restaurants that accept credit cards")
    file.write("\n")
    file.write("Restaurants that accept credit cards \n")
    while (K < N):
        if (B[K] == 1):
            print(A[K])
            file.write(str(A[K]) + "\n")
        K += 1


def stars(file, A, B):
    # local variable
    K = 0
    print("3 Star Restaurants")
    file.write("\n")
    file.write("3 Star Restaurants \n")
    while (K < N):
        if (B[K] >= 3):
            print(A[K])
            file.write(str(A[K]) + "\n")
        K = K + 1


def chinese(file, A, B, C):
    # local variable
    K = 0
    print("Chinese or Thai restaurants that are 3 stars and above ")
    file.write("\n")
    file.write("Chinese or Thai restaurants that are 3 stars and above \n")
    while (K < N):
        if (B[K] == "Chinese" or B[K] == "Thai") and (C[K] >= 3):
            print(A[K])
            file.write(str(A[K]) + "\n")
        K = K + 1


def health(file, A, B):
    # local variable
    K = 0
    print("Restaurants that serve health food")
    file.write("Restaurants that serve health food \n")
    while (K < N):
        if (B[K] == "Health"):
            print(A[K])
            file.write(str(A[K]) + "\n")
        K = K + 1

def ratings(file, A, B):
    #local variable
    R = 1
    while(R < 5):
        K = 0
        print("Restaurants with ", R ," star rating ")
        file.write("\n")
        file.write("Restaurants with " + str(R) + " star rating \n")
        while(K < N):
            if(B[K] == R):
                print(A[K])
                file.write(str(A[K] + "\n"))
            K=K+1
        R=R+1


main()
