#!/usr/bin/env python

import math
import rospy
import traceback

from sami.arm import Arm, EzPose, ArmMotionChain
from sami.gripper import Gripper
from rmi.srv import *
from rmi.msg import *


# Move the arm to an absolute pose.
def move_arm_abs(req):
    try:
        print("Attempting to move arm to [ %s, %s, %s, %s, %s, %s ]"%(req.pose.x, req.pose.y, req.pose.z, req.pose.roll, req.pose.pitch, req.pose.yaw))

        arm = Arm('ur10e', group='manipulator')
        arm.velocity = 0.2

        gripper = Gripper('cr200-85', host='localhost', port=44221)

        pose = [ req.pose.x, req.pose.y, req.pose.z, req.pose.roll, req.pose.pitch, req.pose.yaw ]
        arm.move_pose(pose)

        print("Gripping: %s"%(req.gripping))
        global gripping_state
        if gripping_state != req.gripping:
            if req.gripping:
            	print("(closing gripper)")
            	gripper.grip()
            else:
            	print("(opening gripper")
            	gripper.grip()	# necessary for gripper's state machine ?
            	gripper.release()

    except Exception as e:
        print("Error in arm movement:")
        traceback.print_exc()
        return MoveArmResponse(False)
    return MoveArmResponse(True)


# Move the arm to a pose relative to its current one.
def move_arm_rel(req):
    try:
        print("Attempting to move arm by [ %s, %s, %s, %s, %s, %s ]"%(req.pose.x, req.pose.y, req.pose.z, req.pose.roll, req.pose.pitch, req.pose.yaw))

        arm = Arm('ur10e', group='manipulator')
        arm.velocity = 0.2

        gripper = Gripper('cr200-85', host='localhost', port=44221)

        pose = [ req.pose.x, req.pose.y, req.pose.z, req.pose.roll, req.pose.pitch, req.pose.yaw ]
        arm.move_pose_relative(pose)

        print("Gripping: %s"%(req.gripping))
        global gripping_state
        if gripping_state != req.gripping:
            if req.gripping:
                print("(closing gripper)")
                gripper.grip()
            else:
                print("(opening gripper")
                gripper.grip()  # necessary for gripper's state machine ?
                gripper.release()

    except Exception as e:
        print("Error in arm movement:")
        traceback.print_exc()
        return MoveArmResponse(False)
    return MoveArmResponse(True)


# UNUSED - leftover code from an alternative approach
def move_arm_chain(req):
    try:
        print("Attempting to move arm to [ %s, %s, %s, %s, %s, %s ]"%(req.pose.x, req.pose.y, req.pose.z, req.pose.roll, req.pose.pitch, req.pose.yaw))

        arm = Arm('ur10e', group='manipulator')
        arm.velocity = 0.2

        pose = [ req.pose.x, req.pose.y, req.pose.z, req.pose.roll, req.pose.pitch, req.pose.yaw ]
        
        chain = ArmMotionChain()

        for i in range(0,20):
        	chain.sleep(1).pose_relative(dpose=EzPose(z=0.01))

        arm.move_chain(chain)

    except Exception as e:
        print("Error in arm movement:")
        traceback.print_exc()
        return MoveArmResponse(False)
    return MoveArmResponse(True)


def move_arm_server():
    rospy.init_node('motion_planner', anonymous=True)
    s1 = rospy.Service('move_arm_abs', MoveArm, move_arm_abs)
    s2 = rospy.Service('move_arm_rel', MoveArm, move_arm_rel)
    print("MoveArm service is ready.")
    rospy.spin()


global gripping_state

if __name__ == '__main__':
    gripping_state = True
    move_arm_server()
