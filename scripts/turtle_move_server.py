#!/usr/bin/env python3

from srvtry_pkg.srv import *
from geometry_msgs.msg import Twist
import math
import rospy
import sys
import os

def move_square(lin_vel):
    for i in range(4):

        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        rate = rospy.Rate(5) # 5hz
 
        vel = Twist()
        vel.linear.x = lin_vel 
        vel.linear.y = 0
        vel.linear.z = 0

        for j in range(10): # 10 * 5hz = 2sec
            pub.publish(vel)
            rate.sleep()

        vel = Twist()
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 90*2*math.pi/360*49/10

        pub.publish(vel)
        rate.sleep()

def move_triangle(lin_vel):
    for i in range(3):

        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        rate = rospy.Rate(5) # 3hz
    
        vel = Twist()
        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0
        for j in range(10): # 10 * 5hz = 2sec
            pub.publish(vel)
            rate.sleep()

        vel = Twist()
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 120*2*math.pi/360*5
    
        pub.publish(vel)
        rate.sleep()

def move_circle(lin_vel):

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz
 
    vel = Twist()
    vel.linear.x = lin_vel
    vel.linear.y = 0
    vel.linear.z = 0

    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = lin_vel

    for i in range(60):
        pub.publish(vel)
        rate.sleep()

def handle_move_turtle(req):
    if req.data == 'square':
        print("%s를 그리는 중..."%req.data)
        move_square(req.lin_vel)
        return TurtleMoveResponse(1)
    elif req.data == 'triangle':
        print("%s를 그리는 중..."%req.data)
        move_triangle(req.lin_vel)
        return TurtleMoveResponse(2)
    elif req.data == 'circle':
        print("%s를 그리는 중..."%req.data)
        move_circle(req.lin_vel)
        return TurtleMoveResponse(3)
    else: 
        return TurtleMoveResponse(4)


def move_turtle_server():
    rospy.init_node('move_turtle_server')
    s = rospy.Service('move_turtle', TurtleMove, handle_move_turtle)
    
    rospy.spin()

if __name__ == "__main__":
    move_turtle_server()
