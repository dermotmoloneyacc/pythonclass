# program to multiple matrices
# global variables
sumx = 0
sumy = 0


def main():
    # matrices declaration
    # x[5][3]
    x = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    # y[3][7]
    y = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]
    # z[5][7]
    z = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]
    # variable declaration
    small = 0
    # file declaration
    infilex = open("arrayx.txt", 'r')
    infiley = open("arrayy.txt", 'r')
    outfile = open('lab5.out', 'w')
    # call functions
    loadx(infilex, x)
    loady(infiley, y)
    computez(x, y, z)
    small = smallest(y)
    summation(x, y)
    OUTDATA(outfile, x, y, z)
    # print out other variable
    print("smallest = ", small)
    outfile.write("smallest is " + str(small))
    # print everything
    print("sumx=", sumx)
    outfile.write("sumx =" + str(sumx))
    print("sumy =", sumy)
    outfile.write("sumy = " + str(sumy))
    print("sumx + sumy", sumx + sumy)
    outfile.write("sumx + sumy" + str(sumx + sumy))
    # close files
    infilex.close()
    infiley.close()
    outfile.close()


def loadx(file, A):
    # local variable
    N = 0
    K = 0
    J = 0
    templist = file.readline().strip("\n").split(",")
    print(templist)
    while (K < 5):
        J = 0
        while (J < 3):
            A[K][J] = int(templist[N])
            print(A[K][J])
            J = J + 1
            N = N + 1
        K = K + 1


def loady(file, A):
    # local variable
    N = 0
    K = 0
    J = 0
    templist = file.readline().strip("\n").split(",")
    while (K < 7):
        J = 0
        while (J < 3):
            A[J][K] = int(templist[N])
            print(A[J][K])
            J = J + 1
            N = N + 1
        K = K + 1


def computez(A, B, C):
    # local variable
    I = 0
    J = 0
    K = 0
    while (I < 5):
        J = 0
        while (J < 7):
            K = 0
            while (K < 3):
                C[I][J] = C[I][J] + A[I][K] * B[K][J]
                K = K + 1
            J = J + 1
        I = I + 1


def summation(A, B):
    # global variable
    global sumx
    global sumy
    # local
    K = 0
    while (K < 5):
        sumx = sumx + A[K][2]
        K = K + 1
    K = 0
    while (K < 7):
        sumy = sumy + B[2][K]
        K = K + 1


def smallest(A):
    # local variable
    S = 0
    K = 0
    S = A[1][K]
    K = K + 1
    while (K < 7):
        if (S > A[1][K]):
            S = A[1][K]
        K = K + 1
        return (S)


def OUTDATA(file, A, B, C):
    # local variable
    K = 0
    print("X MATRICES")
    while (K < 5):
        print(A[K][0], A[K][1], A[K][2], "\n")
        file.write(str(A[K][0]) + str(A[K][1]) + str(A[K][2]) + "\n")
        K = K + 1
    print("Y MATRICES")
    K = 0
    while (K < 3):
        print(B[K][0], B[K][1], B[K][2], B[K][3], B[K][4], B[K][5], B[K][6], "\n")
        file.write(str(B[K][0]) + str(B[K][1]) + str(B[K][2]) + str(B[K][3]) +
                   str(B[K][4]) + str(B[K][5]) + str(B[K][6]) + str("\n"))
        K = K + 1
    print("Z MATRICES")
    K = 0
    while (K < 5):
        print(C[K][0], C[K][1], C[K][2], C[K][3], C[K][4], C[K][5], C[K][6], "\n")
        file.write(str(C[K][0]) + str(C[K][1]) + str(C[K][2]) + str(C[K][3]) +
                   str(C[K][4]) + str(C[K][5]) + str(C[K][6]) + str("\n"))
        K = K + 1

main()