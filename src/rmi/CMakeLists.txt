cmake_minimum_required(VERSION 2.8.3)
project(rmi)


find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  gazebo_plugins
  roscpp
  message_generation
  std_msgs
)

find_package(gazebo REQUIRED)

find_package(Protobuf REQUIRED)
find_package(xacro REQUIRED)

add_service_files( DIRECTORY srv
  FILES
  MoveArm.srv
)

catkin_install_python(
  PROGRAMS scripts/move_arm_server.py scripts/move_arm_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
catkin_python_setup()

generate_messages(DEPENDENCIES std_msgs)

catkin_package(
  CATKIN_DEPENDS 
  roscpp
  gazebo_ros
  std_msgs
  message_generation
)


set (CMAKE_CXX_FLAGS " -Wall -std=c++11")


###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)

include_directories(
  plugins/include 
  ${GAZEBO_INCLUDE_DIRS}
  ${catkin_INCLUDE_DIRS}
  )
link_directories(${GAZEBO_LIBRARY_DIRS})

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")
