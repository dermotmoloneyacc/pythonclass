
# Program to calculate the batting average and slugging average
# based on data provided in an input file
# Author DJM
# lab3.py
# ACC Summer 2019
# Professor Onabajo
# Global Variable
N = 9  # number of players


def main():
    # file declaration
    infile = open("lab3.txt", "r")
    outfile = open("lab3.out", "w")
    # variable declaration
    k = 0
    ba = 0.0
    sa = 0.0
    p = 0
    s = d = t = hr = atbat = 0
    S1 = 0
    D1 = 0
    T1 = 0
    HR1 = 0
    # load from datafile and calculate
    k = 0
    while(k < N):
        # yank the first line
        templist = infile.readline().strip("\n").split(",")
        p = int(templist[0])
        # print (p)
        s = int(templist[1])
        # print (s)
        d = int(templist[2])
        # print (d)
        t = int(templist[3])
        # print (t)
        hr = int(templist[4])
        # print (hr)
        atbat = int(templist[5])
        # print (atbat)
        # calculate slugging average ba
        ba = float(s+d+t+hr) / atbat
        # call function to calculate sa
        S1 = single(s)
        D1 = double(d)
        T1 = triple(t)
        HR1 = homerun(hr)
        sa = float(S1+D1+T1+HR1)/atbat
        print(p, ba, sa)
        outfile.write(str(p) + ", \t" + str(ba) + ", \t" + str(sa) + " \n")
        k = k+1
        # close files
        infile.close()
        outfile.close()


def single(x):
    # local variable
    y = 0
    y = x * 1
    return(y)


def double(x):
    # local variable
    y = 0
    y = x * 2
    return(y)


def triple(x):
    # local variable
    y = 0
    y = x * 3
    return(y)


def homerun(x):
    y = 0
    y = x * 4
    return(y)


main()
