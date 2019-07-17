#bubble sort
#author djmoloney
#acc summer 2019 lab7

#global variable
N=20
def main():
    #file declaration
    infile=open("lab7data.txt", "r")
    outfile=open("lab7.out", "w")
    #list declaration
    idx=[0]*N
    score=[0]*N
    #call functions
    loadrec(infile,idx,score)
    #write unsorted data
    print("UNSORTED DATA")
    outfile.write("UNSORTED DATA\n")
    OUTDATA(outfile, idx, score)
    #call bubble sort
    bubble(idx,score)
    print("SORTED DATA")
    outfile.write("SORTED DATA\n")
    OUTDATA(outfile,idx,score)
    #close files
    infile.close()
    outfile.close()
#loadrec
def loadrec(file,A,B):
    #local variable
    K=0
    while(K<N):
        templist=file.readline().strip("\n").split(",")
        A[K]=int(templist[0])
        B[K]=int(templist[1])
        K=K+1

def OUTDATA(file,A,B):
    #local variable
    K=0
    while(K<N):
        print(A[K],B[K])
        file.write(str(A[K]) +" "+ str(B[K])+"\n")
        K=K+1

#bubble sort
def bubble(A,B):
    I=N-1
    flag=1#set flag to start the loop
    while(I>=1)and(flag==1):
        flag=0 #K=0
        J=0
        while(J<=I-1):
            if(A[J] > A[J+1]):
                TEMP=A[J]
                TEMP1=B[J]
                A[J]=A[J+1]
                B[J]=B[J+1]
                A[J+1]=TEMP
                B[J+1]=TEMP1
                flag=1
                J=J+1
            else:
                J=J+1

main()
