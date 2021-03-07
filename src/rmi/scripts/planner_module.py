#!/usr/bin/env python

import os
import rospy

from math import pi, sin, cos
from rmi.srv import *
from rmi.msg import *
from move_arm_client import move_arm_abs, move_arm_rel


# Rotates a vector according to the given rotation matrix
def rotate_vector(rot_matrix, vector):
	new_vector = []
	for i in range(0,3):
		new_vector.append(rot_matrix[i][0]*vector[0]+rot_matrix[i][1]*vector[1]+rot_matrix[i][2]*vector[2])
	# fix floating point errors (on exact 0.0 values)
	#for j in range(0,3):
	#	new_vector[j] = round(new_vector[j], 10)
	return [-vector[2], -vector[0], vector[1]]


# Solves the Tower of Hanoi puzzle
# Given the number of disks and the rod's indexes, returns the list of moves tuples (source, destination).
def get_puzzle_solution(number_of_disks, initial_rod, final_rod, auxiliary_rod):
	moves = []
	if number_of_disks > 0:
		moves = get_puzzle_solution(number_of_disks-1, initial_rod, auxiliary_rod, final_rod)
		moves.append((initial_rod,final_rod))
		moves.extend(get_puzzle_solution(number_of_disks-1, auxiliary_rod, final_rod, initial_rod))
		return moves


def solve_puzzle(initial_rod=0):
	global rod_height
	global disk_height
	global disk_handle_offset
	global number_of_disks
	global rods_pos_adj

	distance_between_rods = []
	for i in range(0,3):
		distance_between_rods.append(abs(rods_pos_adj[0][i]-rods_pos_adj[1][i]))

	# define the height offset (to position the arm) above the rods
	height_offset = rod_height + disk_height

	# rods_pos_above = rods_pos_adj[:]
	# for r in rods_pos_above:
	# 	r[2] += height_offset

	rod_disks = [[],[],[]]
	for i in range(0, number_of_disks):
		rod_disks[initial_rod].append(disk_handle_offset[i])

	# gripper rotation parameters for a better pickup orientation
	roll = 0
	pitch = pi/2
	yaw = pi/2

	# rotation matrix
	rot_x = [cos(yaw)*cos(pitch), cos(yaw)*sin(pitch)*sin(roll)-sin(yaw)*cos(roll), cos(yaw)*sin(pitch)*cos(roll)+sin(yaw)*sin(roll)]
	rot_y = [sin(yaw)*cos(pitch), sin(yaw)*sin(pitch)*sin(roll)+cos(yaw)*cos(roll), sin(yaw)*sin(pitch)*cos(roll)-cos(yaw)*sin(roll)]
	rot_z = [-sin(pitch), cos(pitch)*sin(roll), cos(pitch)*cos(roll)]
	rot_matrix = [rot_x, rot_y, rot_z]

	# move arm to a central position above the rods
	move_arm_abs(PoseCoords(rods_pos_adj[1][0], rods_pos_adj[1][1], rods_pos_adj[1][2]+height_offset, roll, pitch, yaw), False)
	prev_rod = 1
	prev_disk = 0

	moves = get_puzzle_solution(number_of_disks, initial_rod, (initial_rod+1)%3, (initial_rod+2)%3)
	moves.reverse()		# for easier iteration via list (simulating queue)
	while moves:
		# get initial and final rods for the movement
		rod_i,rod_f = moves.pop()
		print("Moving arm from rod %s to rod %s..."%(rod_i, rod_f))

		# get current disk
		curr_disk = rod_disks[rod_i].pop()

		# get (sideways) translation to the top of the initial rod
		dpose_i_top = []
		for i in range(0,3):
			dpose_i_top.append((rod_i-prev_rod)*distance_between_rods[i])
		dpose_i_top[1] -= (curr_disk-prev_disk)		# adjust (y-axis) distance to disk's handle
		vector_i_top = rotate_vector(rot_matrix, dpose_i_top)
		#print(vector_i_top)
		move_arm_rel(PoseCoords(vector_i_top[0], vector_i_top[1], vector_i_top[2], 0, 0, 0), False)

		# get (downwards) translation to the base of the initial rod
		dpose_i_base = [0, 0, -(height_offset - disk_height * len(rod_disks[rod_i]))]
		vector_i_base = rotate_vector(rot_matrix, dpose_i_base)
		#print(vector_i_base)
		move_arm_rel(PoseCoords(vector_i_base[0], vector_i_base[1], vector_i_base[2], 0, 0, 0), True)

		# get (upwards) translation to the top of the initial rod
		dpose_i_top2 = [0, 0, height_offset - disk_height * len(rod_disks[rod_i])]
		vector_i_top2 = rotate_vector(rot_matrix, dpose_i_top2)
		#print(vector_i_top2)
		move_arm_rel(PoseCoords(vector_i_top2[0], vector_i_top2[1], vector_i_top2[2], 0, 0, 0), True)

		# get (sideways) translation to the top of the final rod
		dpose_f_top = []
		for i in range(0,3):
			dpose_f_top.append((rod_f-rod_i)*distance_between_rods[i])
		vector_f_top = rotate_vector(rot_matrix, dpose_f_top)
		#print(vector_f_top)
		move_arm_rel(PoseCoords(vector_f_top[0], vector_f_top[1], vector_f_top[2], 0, 0, 0), True)

		# get (downwards) translation to the base of the final rod
		dpose_f_base = [0, 0, -(height_offset - disk_height * len(rod_disks[rod_f]))]
		vector_f_base = rotate_vector(rot_matrix, dpose_f_base)
		#print(vector_f_base)
		move_arm_rel(PoseCoords(vector_f_base[0], vector_f_base[1], vector_f_base[2], 0, 0, 0), False)

		# get (upwards) translation to the top of the final rod
		dpose_f_top2 = [0, 0, height_offset - disk_height * len(rod_disks[rod_f])]
		vector_f_top2 = rotate_vector(rot_matrix, dpose_f_top2)
		#print(vector_f_top2)
		move_arm_rel(PoseCoords(vector_f_top2[0], vector_f_top2[1], vector_f_top2[2], 0, 0, 0), False)

		rod_disks[rod_f].append(curr_disk)
		prev_rod = rod_f
		prev_disk = curr_disk

	# move arm to a central position above the rods
	move_arm_abs(PoseCoords(rods_pos_adj[1][0], rods_pos_adj[1][1], rods_pos_adj[1][2]+height_offset, roll, pitch, yaw), False)


def setup_puzzle(initial_rod=0):
	global rod_height
	global rod_base_height
	global disk_height
	global gripper_length
	global disk_handle_offset
	global number_of_disks
	global rods_pos_adj

	# define the height offset (to position the arm) above the rods
	height_offset = rod_height + disk_height

	# gripper rotation parameters for a better pickup orientation
	roll = 0
	pitch = pi/2
	yaw = pi/2

	# rotation matrix
	rot_x = [cos(yaw)*cos(pitch), cos(yaw)*sin(pitch)*sin(roll)-sin(yaw)*cos(roll), cos(yaw)*sin(pitch)*cos(roll)+sin(yaw)*sin(roll)]
	rot_y = [sin(yaw)*cos(pitch), sin(yaw)*sin(pitch)*sin(roll)+cos(yaw)*cos(roll), sin(yaw)*sin(pitch)*cos(roll)-cos(yaw)*sin(roll)]
	rot_z = [-sin(pitch), cos(pitch)*sin(roll), cos(pitch)*cos(roll)]
	rot_matrix = [rot_x, rot_y, rot_z]

	# get the disks position on the table
	disks_pos = []
	for disk in range(0, number_of_disks):
		rospy.loginfo("Waiting for disk (pose) perception service...")
		rospy.wait_for_service('get_ring_pose')
		try:
			rospy.loginfo("Requesting pose of disk %s."%(disk))
			disk_srv = rospy.ServiceProxy('get_ring_pose', GetRingPose)
			disk_pose = disk_srv.call(GetRingPoseRequest(ring_id=disk))
			disks_pos[disk] = list(disk_pose.pose)
		except rospy.ServiceException as e:
			rospy.logerr("Service call failed:\n%s", e)

	# pickup each disk and put it in the initial rod
	for disk in range(0, number_of_disks):
		print("Picking up disk %s at %s."%(disk, disks_pos[disk]))

		# move arm to the position directly above the disk to pickup
		move_arm_abs(PoseCoords(disks_pos[disk][0], disks_pos[disk][1], disks_pos[disk][2]+height_offset+rod_base_height+gripper_length, roll, pitch, yaw), False)

		# get (downwards) translation to the disk on the table
		dpose_i_base = [0, 0, -(height_offset + rod_base_height)]
		vector_i_base = rotate_vector(rot_matrix, dpose_i_base)
		#print(vector_i_base)
		move_arm_rel(PoseCoords(vector_i_base[0], vector_i_base[1], vector_i_base[2], 0, 0, 0), True)

		# get (upwards) translation to above the table
		dpose_i_top = [0, 0, height_offset + rod_base_height]
		vector_i_top = rotate_vector(rot_matrix, dpose_i_top)
		#print(vector_i_top)
		move_arm_rel(PoseCoords(vector_i_top[0], vector_i_top[1], vector_i_top[2], 0, 0, 0), True)

		# get (sideways: x- and y-axis) translation to the top of the destination rod
		dpose_f_top = []
		dpose_f_top.append(rods_pos_adj[initial_rod][0]- disks_pos[disk][0])	# x-axis
		dpose_f_top.append(rods_pos_adj[initial_rod][1]- disks_pos[disk][1])	# y-axis
		dpose_f_top.append(0)	# z-axis
		vector_f_top = rotate_vector(rot_matrix, dpose_f_top)
		#print(vector_f_top)
		move_arm_rel(PoseCoords(vector_f_top[0], vector_f_top[1], vector_f_top[2], 0, 0, 0), True)

		# get (downwards) translation to the base of the destination rod
		dpose_f_base = [0, 0, -(height_offset - disk_height * disk)]
		vector_f_base = rotate_vector(rot_matrix, dpose_f_base)
		#print(vector_f_base)
		move_arm_rel(PoseCoords(vector_f_base[0], vector_f_base[1], vector_f_base[2], 0, 0, 0), False)

		# get (upwards) translation to the top of the destination rod
		dpose_f_top2 = [0, 0, height_offset - disk_height * disk]
		vector_f_top2 = rotate_vector(rot_matrix, dpose_f_top2)
		#print(vector_f_top2)
		move_arm_rel(PoseCoords(vector_f_top2[0], vector_f_top2[1], vector_f_top2[2], 0, 0, 0), False)


# Spawns the disks models in a tower rod (ready) or random positions of the simulation world.
def spawn_models(ready_positions, initial_rod=0):
	if ready_positions:
		os.system("rosrun gazebo_ros spawn_model -sdf -database hanoi_ring_3 -model ring3 -x -0.15 -y 0.7 -z 0.73 -Y " + str(pi))
		os.system("rosrun gazebo_ros spawn_model -sdf -database hanoi_ring_2 -model ring2 -x -0.15 -y 0.7 -z 0.77 -Y " + str(pi))
		os.system("rosrun gazebo_ros spawn_model -sdf -database hanoi_ring_1 -model ring1 -x -0.15 -y 0.7 -z 0.81 -Y " + str(pi))
	else:
		# TODO: setup an area to give as a random possible interval
		os.system("rosrun gazebo_ros spawn_model -sdf -database hanoi_ring_3 -model ring3 -x -0.15 -y 0.5 -z 0.71 -Y " + str(pi))
		os.system("rosrun gazebo_ros spawn_model -sdf -database hanoi_ring_2 -model ring2 -x 0 -y 0.5 -z 0.71 -Y " + str(pi))
		os.system("rosrun gazebo_ros spawn_model -sdf -database hanoi_ring_1 -model ring1 -x 0.15 -y 0.5 -z 0.71 -Y " + str(pi))


# Gets the information relative to models sizes and positions.
def get_simulation_parameters():
	rospy.loginfo("Waiting for parameter provider service...")
	rospy.wait_for_service('get_param')
	try:
		rospy.loginfo("Requesting simulation parameters.")
		par_srv = rospy.ServiceProxy('get_param', GetParam)
		sim_par = par_srv.call(GetParamRequest())
	except rospy.ServiceException as e:
		rospy.logerr("Service call failed:\n%s", e)
	global rod_height
	rod_height = sim_par.rod_height
	global rod_base_height
	rod_base_height = sim_par.rod_base_height
	global disk_height
	disk_height = sim_par.disk_height
	global gripper_length
	gripper_length = sim_par.gripper_length
	global disk_handle_offset
	disk_handle_offset = list(sim_par.disk_handle_offset)
	global number_of_disks
	number_of_disks = sim_par.number_of_disks
	# round values to 2dp to fix floating point errors (from message transfer) ?

	rospy.loginfo("Waiting for parameter provider service...")
	rospy.wait_for_service('get_rod_pos')
	try:
		rospy.loginfo("Requesting simulation parameters.")
		rod_pos_srv = rospy.ServiceProxy('get_rod_pos', GetRodPos)
		rpos = rod_pos_srv.call(GetRodPosRequest())
	except rospy.ServiceException as e:
		rospy.logerr("Service call failed:\n%s", e)
	global rods_pos
	rods_pos = [list(rpos.left_rod), list(rpos.middle_rod), list(rpos.right_rod)]
	global rods_pos_adj
	rods_pos_adj = rods_pos[:]
	# adjust height with the gripper length offset
	for r in rods_pos_adj:
		r[2] += gripper_length


# Global variables with some parameter values
global rod_height
global rod_base_height
global disk_height
global gripper_length
global disk_handle_offset
global number_of_disks
global rods_pos
global rods_pos_adj

if __name__ == '__main__':
	get_simulation_parameters()
	#print("Simulation parameters:\n\tRod height= %s\n\tRod base height= %s\n\tDisk height= %s\n\tGripper length= %s\n\tDisk handle offsets= %s\n\tNumber of disks= %s"%(rod_height, disk_height, gripper_length, disk_handle_offset,number_of_disks))
	#print("Rod coordinates:\n\t%s\n\t%s\n\t%s"%(rods_pos[0], rods_pos[1], rods_pos[2]))
	initial_rod = 0
	puzzle_ready = False
	#spawn_models(puzzle_ready, initial_rod)
	if not puzzle_ready:
		setup_puzzle(initial_rod)
	print("Puzzle ready to be solved.")
	#solve_puzzle(initial_rod)
	print("Puzzle solved!")
