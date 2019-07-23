#Statistical Program
#Compute standard deviation using lists/array
#Name: dmoloney
#ACC Summer 2019
#Lab4.py
#Prof Onabajo
#Global Variable
import math
N=20
def main():
    #file declaration
    infile=open("lab4.txt","r")
    outfile=open("lab4.out","w")
    #variable declaration
    sumx=0.0
    std=0.0
    SD2=0.0
    xbar=0.0
    #List/Array declarations
    x=[0.0]*N
    DEV=[0.0]*N
    DEV1=[0.0]*N
    SD1=[0.0]*N
    #call functions
    sumx=LOADDATA(infile, x)
    print(sumx)
    #compute average
    xbar=sumx/N
    print(xbar)
    #Call function deviation
    DEV2=DEVIATION(x, DEV, DEV1, xbar)
    #compute standard deviation
    std=math.sqrt(DEV2/N)
    #function to compute standard score
    SD2=STANDARD(DEV1,SD1,std)
    #call OUTDATA
    OUTDATA(outfile, x, DEV, DEV1, SD1)
    #PRINT THE REST OF THE OUTPUT
    print("SUM= ",sumx)
    outfile.write("SUM= " + str(sumx))
    print("Average = ", xbar)
    print ("Standard Deviation = ",std)
    print ("STD score = ",SD2)
    #close file
    infile.close()
    outfile.close()
def LOADDATA(infile, A):
    #local variables
    B=0
    K=0
    while(K<N):
        templist=infile.readline().split(",")
        A[K] = float(templist[0])
        print(A[K])
        B=B+A[K]
        K=K+1
    return(B)
def DEVIATION(A,B,C,d):
    #local variable
    e=0
    K=0
    while(K<N):
        B[K]=d-A[K]
        C[K]=B[K]*B[K]
        e=e+C[K]
        K=K+1
    return(e)
def STANDARD(A,B,c):
    #Local variable
    d=0
    K=0
    while (K<N):
        B[K]=A[K]/c
        d=d+B[K]
        K=K+1
    return(d)
def OUTDATA(file, A,B,C,D):
    #Local variable
    K=0
    while(K<N):
            print(A[K],B[K],C[K],D[K])
            file.write(str(A[K]) + " \t" + str(B[K]) + " \t" + str(C[K]) + " \t" + str(D[K]) + " \n")
            K=K+1


main()
