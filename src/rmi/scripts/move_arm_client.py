#!/usr/bin/env python

import rospy
import sys

from rmi.srv import *
from rmi.msg import *


# Request service to move the arm to an absolute pose.
def move_arm_abs(pose, gripping):
    rospy.loginfo("Waiting for move_arm_abs service...")
    rospy.wait_for_service('move_arm_abs')
    try:
        rospy.loginfo("Requesting to move arm to [ %s, %s, %s, %s, %s, %s ] with gripping %s"%(pose.x, pose.y, pose.z, pose.roll, pose.pitch, pose.yaw, gripping))
        move_arm = rospy.ServiceProxy('move_arm_abs', MoveArm)
        resp = move_arm.call(MoveArmRequest(pose, gripping))
        return resp.success
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed:\n%s", e)


# Request service to move the arm to a pose relative to its current one.
def move_arm_rel(pose, gripping):
    rospy.loginfo("Waiting for move_arm_rel service...")
    rospy.wait_for_service('move_arm_rel')
    try:
        rospy.loginfo("Requesting to move arm by [ %s, %s, %s, %s, %s, %s ] with gripping %s"%(pose.x, pose.y, pose.z, pose.roll, pose.pitch, pose.yaw, gripping))
        move_arm = rospy.ServiceProxy('move_arm_rel', MoveArm)
        resp = move_arm.call(MoveArmRequest(pose, gripping))
        return resp.success
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed:\n%s", e)


if __name__ == '__main__':
    argv = rospy.myargv()
    if len(argv) == 9 and argv[1] in ["abs", "rel"]:
        try:
            x = float(argv[2])
            y = float(argv[3])
            z = float(argv[4])
            roll = float(argv[5])
            pitch = float(argv[6])
            yaw = float(argv[7])
            gripping = argv[8].lower() == "true"
        except:
            print("Args: abs/rel x y z roll pitch yaw gripping")
            sys.exit(1)
    else:
        print("Args: abs/rel x y z roll pitch yaw gripping")
        sys.exit(1)

    pose = PoseCoords(x, y, z, roll, pitch, yaw)
    if [argv[1] == "rel"]:
        print(move_arm_rel(pose, gripping))
    else:
        print(move_arm_abs(pose, gripping))
