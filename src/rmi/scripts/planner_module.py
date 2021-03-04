#!/usr/bin/env python

import os

from math import pi, sin, cos
from sim_par import *
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
def solve_puzzle(number_of_disks, initial_rod, final_rod, auxiliary_rod):
	moves = []
	if number_of_disks > 0:
		moves = move(number_of_disks-1, initial_rod, auxiliary_rod, final_rod)
		moves.append("(%s,%s)"%(initial_rod,final_rod))
		moves.extend(move(number_of_disks-1, auxiliary_rod, final_rod, initial_rod))
		return moves


def main():
	# calculate the rods' coordinates
	rods_pos = [[], [], []]
	rods_pos[1] = MIDDLE_ROD_POS
	for i in range(0,3):
		rods_pos[0].append(MIDDLE_ROD_POS[i] - DISTANCE_BETWEEN_RODS[i])
		rods_pos[2].append(MIDDLE_ROD_POS[i] + DISTANCE_BETWEEN_RODS[i])

	# adjust height with the gripper length offset
	for r in rods_pos:
		r[2] += GRIPPER_LENGTH

	# rods_pos_above = rods_pos.copy()
	# for r in rods_pos_above:
	# 	r[2] += ROD_HEIGHT + DISK_HEIGHT

	initial_rod = 0
	rod_disks = [[],[],[]]
	for i in range(0, N_DISKS):
		rod_disks[initial_rod].append(DISTANCE_DISK_HOLE_TO_HANDLE[i])

	roll = 0
	pitch = pi/2
	yaw = pi/2

	# rotation matrix
	rot_x = [cos(yaw)*cos(pitch), cos(yaw)*sin(pitch)*sin(roll)-sin(yaw)*cos(roll), cos(yaw)*sin(pitch)*cos(roll)+sin(yaw)*sin(roll)]
	rot_y = [sin(yaw)*cos(pitch), sin(yaw)*sin(pitch)*sin(roll)+cos(yaw)*cos(roll), sin(yaw)*sin(pitch)*cos(roll)-cos(yaw)*sin(roll)]
	rot_z = [-sin(pitch), cos(pitch)*sin(roll), cos(pitch)*cos(roll)]
	rot_matrix = [rot_x, rot_y, rot_z]

	# define the height offset (to position the arm) above the rods
	height_offset = ROD_HEIGHT + DISK_HEIGHT

	# move arm to a central position above the rods
	move_arm_abs(PoseCoords(rods_pos[1][0], rods_pos[1][1], rods_pos[1][2]+height_offset, roll, pitch, yaw), False)
	prev_rod = 1
	prev_disk = 0

	moves = solve_puzzle(N_DISKS, initial_rod, (initial_rod+1)%3, (initial_rod+2)%3)
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
			dpose_i_top.append((rod_i-prev_rod)*DISTANCE_BETWEEN_RODS[i])
		dpose_i_top[1] -= (curr_disk-prev_disk)		# adjust (y-axis) distance to disk's handle
		vector_i_top = rotate_vector(rot_matrix, dpose_i_top)
		print(vector_i_top)
		move_arm_rel(PoseCoords(vector_i_top[0], vector_i_top[1], vector_i_top[2], 0, 0, 0), False)

		# get (downwards) translation to the base of the initial rod
		dpose_i_base = [0, 0, -(height_offset - DISK_HEIGHT * len(rod_disks[rod_i]))]
		vector_i_base = rotate_vector(rot_matrix, dpose_i_base)
		print(vector_i_base)
		move_arm_rel(PoseCoords(vector_i_base[0], vector_i_base[1], vector_i_base[2], 0, 0, 0), True)

		# get (upwards) translation to the top of the initial rod
		dpose_i_top2 = [0, 0, height_offset - DISK_HEIGHT * len(rod_disks[rod_i])]
		vector_i_top2 = rotate_vector(rot_matrix, dpose_i_top2)
		print(vector_i_top2)
		move_arm_rel(PoseCoords(vector_i_top2[0], vector_i_top2[1], vector_i_top2[2], 0, 0, 0), True)

		# get (sideways) translation to the top of the final rod
		dpose_f_top = []
		for i in range(0,3):
			dpose_f_top.append((rod_f-rod_i)*DISTANCE_BETWEEN_RODS[i])
		vector_f_top = rotate_vector(rot_matrix, dpose_f_top)
		print(vector_f_top)
		move_arm_rel(PoseCoords(vector_f_top[0], vector_f_top[1], vector_f_top[2], 0, 0, 0), True)

		# get (downwards) translation to the base of the final rod
		dpose_f_base = [0, 0, -(height_offset - DISK_HEIGHT * len(rod_disks[rod_f]))]
		vector_f_base = rotate_vector(rot_matrix, dpose_f_base)
		print(vector_f_base)
		move_arm_rel(PoseCoords(vector_f_base[0], vector_f_base[1], vector_f_base[2], 0, 0, 0), False)

		# get (upwards) translation to the top of the final rod
		dpose_f_top2 = [0, 0, height_offset - DISK_HEIGHT * len(rod_disks[rod_f])]
		vector_f_top2 = rotate_vector(rot_matrix, dpose_f_top2)
		print(vector_f_top2)
		move_arm_rel(PoseCoords(vector_f_top2[0], vector_f_top2[1], vector_f_top2[2], 0, 0, 0), False)

		rod_disks[rod_f].append(curr_disk)
		prev_rod = rod_f
		prev_disk = curr_disk

	# move arm to a central position above the rods
	move_arm_abs(PoseCoords(rods_pos[1][0], rods_pos[1][1], rods_pos[1][2]+height_offset, roll, pitch, yaw), False)


def main2():
	rod_pos = [MIDDLE_ROD_POS-DISTANCE_BETWEEN_RODS,
				MIDDLE_ROD_POS,
				MIDDLE_ROD_POS+DISTANCE_BETWEEN_RODS]
	for r in rod_pos:
		r[2] += GRIPPER_LENGTH

	rod_disks = [3, 0, 0]

	roll = 0
	pitch = math.pi/2
	yaw = math.pi/2

	moves = solve_puzzle(N_DISKS)
	moves.reverse()		# for easier iteration via list (simulating queue)
	while moves:
		# get initial and final rods for the movement
		rod_i,rod_f = moves.pop()
		# get initial rod coordinates
		pose_i = rod_pos[rod_i].copy()
		# add the (height/z) offset for the current amount of disks in the rod
		pose_i[2] += DISK_HEIGHT * (rod_disks[rod_i]-1)
		# request movement
		move_arm_abs(PoseCoords(pose_i[0], pose_i[1], pose_i[2], roll, pitch, yaw), True)

		# get initial rod coordinates
		pose_i_setup = rod_pos[rod_i].copy()
		# add the (height/z) offset to a position above the rods
		pose_i_setup[2] += ROD_HEIGHT + DISK_HEIGHT
		# request chainned movement ("smoother"/more linear)
		move_arm_abs(PoseCoords(pose_i_setup[0], pose_i_setup[1], pose_i_setup[2], roll, pitch, yaw), True)


def setup_puzzle():
	# spawn models?
	os.system("rosrun gazebo_ros spawn_model -sdf -database hanoi_ring_3 -model ring3 -x -0.15 -y 0.7 -z 0.73 -Y " + str(pi))
	os.system("rosrun gazebo_ros spawn_model -sdf -database hanoi_ring_2 -model ring2 -x -0.15 -y 0.7 -z 0.77 -Y " + str(pi))
	os.system("rosrun gazebo_ros spawn_model -sdf -database hanoi_ring_1 -model ring1 -x -0.15 -y 0.7 -z 0.81 -Y " + str(pi))
	pass


if __name__ == '__main__':
	puzzle_ready = False
	if not puzzle_ready:
		setup_puzzle()
	print("Puzzle ready to be solved.")
	main()
	print("Puzzle solved!")
