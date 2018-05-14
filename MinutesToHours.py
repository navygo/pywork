#!/usr/bin/env python3
import sys
import math

def MinuToHours(v_min):
    #print(v_min)
    h =math.floor(v_min / 60)
    m =v_min % 60
    #print(h,m)
    print("{:d} H,{:d} M".format(h,m))

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Please add para min")
        sys.exit(1)
    #print(sys.argv)
    h=sys.argv[1]
    #print(h)
    
    try:
        MinuToHours(int(h))
    except:
        print("Input number cannot be negative")
