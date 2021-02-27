execute_process(COMMAND "/home/ubuntu/Desktop/ur10e-hanoi/build/rmi/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/ubuntu/Desktop/ur10e-hanoi/build/rmi/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
