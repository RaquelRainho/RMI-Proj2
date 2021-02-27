#!/usr/bin/env python

import rospy
import sys

from rmi.srv import *

def move_arm_client(x, y, z, roll, pitch, yaw, gripping):
    print("Waiting for MoveArm service...")
    rospy.wait_for_service('move_arm')
    try:
        print("Requesting to move arm to [ %s, %s, %s, %s, %s, %s ] with gripping %s"%(x, y, z, roll, pitch, yaw, gripping))
        move_arm = rospy.ServiceProxy('move_arm', MoveArm)
        resp = move_arm.call(MoveArmRequest(x, y, z, roll, pitch, yaw, gripping))
        return resp.success
    except rospy.ServiceException as e:
        print("Service call failed:", e)

if __name__ == '__main__':
    argv = rospy.myargv()
    if len(argv) == 8:
        try:
            x = float(argv[1])
            y = float(argv[2])
            z = float(argv[3])
            roll = float(argv[4])
            pitch = float(argv[5])
            yaw = float(argv[6])
            gripping = bool(argv[7])
        except:
            print("Args: x y z roll pitch yaw gripping")
            sys.exit(1)
    else:
        print("Args: x y z roll pitch yaw gripping")
        sys.exit(1)
    print(move_arm_client(x, y, z, roll, pitch, yaw, gripping))
