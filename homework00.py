#!/usr/bin/python2
import rospy
inp = input()
n1 = int(input())
n2 = int(input())
if inp == 1:
        print("{:.2f}".format(n1+n2))
elif inp == 2:
        print("{:.2f}".format(n1-n2))

