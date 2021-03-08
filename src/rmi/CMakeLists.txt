cmake_minimum_required(VERSION 2.8.3)
project(rmi)


find_package(catkin REQUIRED COMPONENTS
  gazebo_ros
  gazebo_plugins
  roscpp
  rospy
  message_generation
  std_msgs
  pcl_conversions
  pcl_ros
  sensor_msgs
)

find_package(gazebo REQUIRED)

find_package(Protobuf REQUIRED)
find_package(xacro REQUIRED)
find_package(OpenCV REQUIRED)

add_service_files( DIRECTORY srv
  FILES
  MoveArm.srv
  GetRingPose.srv
  GetParam.srv
  GetRodPos.srv
)

add_message_files(
  FILES
  PoseCoords.msg
)

catkin_install_python(
  PROGRAMS
  scripts/move_arm_server.py
  scripts/move_arm_client.py
  scripts/param_provider.py
  scripts/planner_module.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
catkin_python_setup()

generate_messages(DEPENDENCIES std_msgs)

catkin_package(
  CATKIN_DEPENDS 
  roscpp
  gazebo_ros
  std_msgs
  message_runtime
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
  ${OpenCV_INCLUDE_DIRS}
  )

include_directories(  ${catkin_INCLUDE_DIRS}  ${OpenCV_INCLUDE_DIRS} )

link_directories(
  ${GAZEBO_LIBRARY_DIRS}
  )


add_executable(perception_module scripts/perception_module.cpp)
target_link_libraries(perception_module ${catkin_LIBRARIES})
add_dependencies(perception_module ${rmi_EXPORTED_TARGETS})

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${GAZEBO_CXX_FLAGS}")

