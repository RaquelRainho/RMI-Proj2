#!/usr/bin/env python

import math
import rospy

from sami.arm import Arm, EzPose, ArmMotionChain
from sami.gripper import Gripper

def main():
    rospy.init_node('motion_planner', anonymous=True)

    arm = Arm('ur10e', group='manipulator')
    arm.velocity = 0.2

    arm.move_pose_relative(dpose=EzPose(z=0.22))

    # arm.move_pose_relative(dpose=EzPose(yaw=math.pi*0.25), velocity=0.5)
    # arm.move_pose_relative(dpose=EzPose(yaw=-math.pi*0.25), velocity=0.05)


if __name__ == '__main__':
    main()
