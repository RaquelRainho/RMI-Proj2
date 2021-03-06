#!/usr/bin/env python

import math
import rospy
import traceback

from rmi.srv import *
from rmi.msg import *


# Provide the simulation parameters (mostly related to model sizes).
def get_param(req):
    try:
        rod_height=0.18
        disk_height=0.04
        gripper_length= 0.1
        disk_handle_offset=[0.07,0.06,0.06]
        number_of_disks=3
        rospy.loginfo("Simulation parameters:\n\tRod height= %s\n\tDisk height= %s\n\tGripper length= %s\n\tDisk handle offsets= %s\n\tNumber of disks= %s"%(rod_height, disk_height, gripper_length, disk_handle_offset,number_of_disks))
        resp = GetParamResponse(rod_height=rod_height, disk_height=disk_height, gripper_length=gripper_length, disk_handle_offset=disk_handle_offset, number_of_disks=number_of_disks)
    except Exception as e:
        rospy.logerr("Error in the parameters provider.")
        traceback.print_exc()
        return None
    return resp


# Provide the coordinates to the 3 rods positions.
def get_rod_pos(req):
    try:
        left_rod=[-0.15, 0.7, 0.03]
        middle_rod=[0, 0.7, 0.03]
        right_rod=[0.15, 0.7, 0.03]
        rospy.loginfo("Rod coordinates:\n\t%s\n\t%s\n\t%s"%(left_rod, middle_rod, right_rod))
        resp = GetRodPosResponse(left_rod=left_rod, middle_rod=middle_rod, right_rod=right_rod)
    except Exception as e:
        rospy.logerr("Error in the parameters provider.")
        traceback.print_exc()
        return None
    return resp


def param_prov_server():
    rospy.init_node('parameter_provider', anonymous=True)
    s1 = rospy.Service('get_param', GetParam, get_param)
    s2 = rospy.Service('get_rod_pos', GetRodPos, get_rod_pos)
    rospy.loginfo("Parameter provider service is ready.")
    rospy.spin()


if __name__ == '__main__':
    param_prov_server()
