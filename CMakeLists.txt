cmake_minimum_required(VERSION 3.0.2)
project(super_robot_package)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

catkin_package()

# УСТАНОВКА ВСЕХ LAUNCH-ФАЙЛОВ
install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "*"
)
