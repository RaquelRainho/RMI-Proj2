#!/usr/bin/env python

import rospy
import sys

from rmi.srv import *
from rmi.msg import *

def move_arm_client(pose, gripping):
    print("Waiting for MoveArm service...")
    rospy.wait_for_service('move_arm')
    try:
        print("Requesting to move arm to [ %s, %s, %s, %s, %s, %s ] with gripping %s"%(pose.x, pose.y, pose.z, pose.roll, pose.pitch, pose.yaw, gripping))
        move_arm = rospy.ServiceProxy('move_arm', MoveArm)
        resp = move_arm.call(MoveArmRequest(pose, gripping))
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
            gripping = argv[7].lower() == "true"
        except:
            print("Args: x y z roll pitch yaw gripping")
            sys.exit(1)
    else:
        print("Args: x y z roll pitch yaw gripping")
        sys.exit(1)

    pose = PoseCoords(x, y, z, roll, pitch, yaw)
    print(move_arm_client(pose, gripping))
