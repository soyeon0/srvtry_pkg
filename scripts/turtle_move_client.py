#!/usr/bin/env python3

import sys
import rospy
import os
import string
from srvtry_pkg.srv import *
 
rospy.init_node('move_turtle_client')

def mode():
    print('Enter Mode : ')
    x = str(input())
    if x == "square":
        print('Distace : ')
        y = int(input())
    elif x == "triangle":
        print('Distance : ')
        y = int(input())
    elif x == "circle":
        print('Size : ')
        y = int(input())
    else:
        x,y = 0
    move_turtle_client(x, y)

def move_turtle_client(x, y):
    rospy.wait_for_service('move_turtle')
    try:
        move_turtle = rospy.ServiceProxy('move_turtle', TurtleMove)
        resp = move_turtle(x, y)
        return resp
       
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

while not rospy.is_shutdown():

    mode()
    


