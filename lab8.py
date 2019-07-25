# Program to calculate the batting average and slugging average
# based on data provided in an input file
# Author DJM
# lab8.py
# ACC Summer 2019
# Professor Onabajo
# Global Variable
import baseball
N = 9  # number of players


def main():
    base = baseball.baseball()
    # variable declaration
    p = 0
    s = 0
    d = 0
    t = 0
    # file declaration
    infile = open("lab8.txt", "r")
    outfile = open("lab8.out", "w")
    hr = 0
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
        s1 = base.single(s)
        d1 = base.double(d)
        t1 = base.triple(t)
        hr1 = base.homerun(hr)
        sa = float(s1+d1+t1+hr1)/atbat
        print(p, ba, sa)
        outfile.write(str(p) + ", \t" + str(ba) + ", \t" + str(sa) + " \n")
        k = k+1
        # close files
    infile.close()
    outfile.close()
main()