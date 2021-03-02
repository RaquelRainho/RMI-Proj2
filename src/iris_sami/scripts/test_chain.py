#!/usr/bin/env python

import math
import rospy

from sami.arm import Arm, EzPose, ArmMotionChain
from sami.gripper import Gripper

def main():
    rospy.init_node('motion_planner', anonymous=True)

    arm = Arm('ur10e', group='manipulator')
    arm.velocity = 0.2

    x = 0.0
    y = 0.64
    z = 0.33
    roll = 0.0
    pitch = math.pi/2
    yaw = math.pi/2
    chain = ArmMotionChain()

    #for i in range(1,21):
    #    chain.pose(pose=[x, y, z-i*0.01, roll, pitch, yaw])
    
    chain.pose(pose=[x, y, z-0.20, roll, pitch, yaw])

    arm.move_chain(chain)

if __name__ == '__main__':
    main()
