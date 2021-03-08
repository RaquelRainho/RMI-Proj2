# RMI-Proj2
Solving the Towers of Hanoi puzzle using the UR10e robot arm (in a simulation environment). 

--- 

Dependencies: 
- ROS Melodic
- Gazebo
- Python 2.7 

#### How to run 

Build the project: 
`catkin build`

Execute in every shell used:
`. devel/setup.bash` 

Run the main launch file (with grasp plugin): 
`roslaunch rmi sim.launch load_grasp_fix:=true` 

Run the solver script (planner module): 
`rosrun rmi planner_module.py`