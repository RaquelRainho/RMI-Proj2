#!/usr/bin/env python

import math
import rospy
import traceback

from sami.arm import Arm, EzPose, ArmMotionChain
from sami.gripper import Gripper
from rmi.srv import *

def move_arm(req):
    try:
        print("Attempting to move arm to [ %s, %s, %s, %s, %s, %s ]"%(req.x, req.y, req.z, req.roll, req.pitch, req.yaw))
        #rospy.init_node('motion_planner', anonymous=True)

        arm = Arm('ur10e', group='manipulator')
        arm.velocity = 0.2

        #gripper = Gripper('cr200-85', host='localhost', port=44221)

        pose = [ req.x, req.y, req.z, req.roll, req.pitch, req.yaw ]
        arm.move_pose(pose)
        #arm.move_pose_relative(dpose=EzPose(yaw=math.pi*0.25), velocity=0.4)
        
        #arm.move_pose(pose=[x, y, 0.6, 0, 0.5, math.pi + math.pi/6])
        # arm.move_pose(pose=[x, y, 0.5, 0, math.pi*0.5, math.atan2(y,x)])
        # print math.atan2(y,x)

        # arm.move_pose_relative(dpose=EzPose(yaw=math.pi*0.25), velocity=0.5)
        # arm.move_pose_relative(dpose=EzPose(yaw=-math.pi*0.25), velocity=0.05)

        print("Gripping: %s"%(req.gripping))
        if req.gripping:
        	print("(closing gripper)")
            #gripper.grip()
        else:
        	print("(opening gripper")
        	#gripper.grip()	# necessary for gripper's state machine ?
        	#gripper.release()

        # a = 0.3
        # chain = ArmMotionChain()
        # chain.sleep(2).pose_relative(dpose=EzPose(yaw=a))
        # chain.sleep(2).pose_relative(dpose=EzPose(yaw=-2*a))
        # chain.sleep(2).pose_relative(dpose=EzPose(yaw=a))
        # chain.pose_relative(dpose=EzPose(pitch=a))
        # chain.sleep(2).pose_relative(dpose=EzPose(pitch=-2*a))
        # chain.sleep(2).pose_relative(dpose=EzPose(pitch=a))
        # chain.pose_relative(dpose=EzPose(x=0.1))
        # chain.sleep(2).pose_relative(dpose=EzPose(roll=0.5))
        # chain.sleep(2).pose_relative(dpose=EzPose(roll=-1.0))
        # chain.sleep(2).pose_relative(dpose=EzPose(roll=0.5))
        # chain.sleep(2).pose_relative(dpose=EzPose(x=-0.1))

        # arm.move_chain(chain)

    except Exception as e:
        print("Error in arm movement:")
        traceback.print_exc()
        return MoveArmResponse(False)
    return MoveArmResponse(True)

def move_arm_server():
    rospy.init_node('motion_planner', anonymous=True)
    s = rospy.Service('move_arm', MoveArm, move_arm)
    print("MoveArm service is ready.")
    rospy.spin()

if __name__ == '__main__':
    move_arm_server()
