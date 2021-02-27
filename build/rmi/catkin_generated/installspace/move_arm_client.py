#!/usr/bin/env python2

import rospy
import sys

def move_arm_client(x, y, z, roll, pitch, yaw, gripping):
    rospy.wait_for_service('move_arm_server')
    try:
        move_arm = rospy.ServiceProxy('move_arm_server', MoveArm)
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
            print(sys.argv[0], "x y z roll pitch yaw gripping")
    else:
        print(sys.argv[0], "x y z roll pitch yaw gripping")
    print(move_arm_client(x, y, z, roll, pitch, yaw, gripping))
