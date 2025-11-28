#!/usr/bin/env python3
import rospy

rospy.init_node('params_study')

distro = rospy.get_param('/rosdistro')
my_set_param = rospy.get_param('my_set', 'default_value')
my_private_param = rospy.get_param('~private_param', 'default_private')

rospy.set_param('~ros_priv_param', 'Hi, I am private =)')
rospy.set_param('ros_loc_param', 'Hi, I am local =)')
rospy.set_param('/ros_glob_param', 'Hi, I am global =)')
not_exist_param = rospy.get_param('i_do_not_exist', 'default_value')

param_name_2_delete = '/ros_glob_param'


param_list = rospy.get_param_names()
rospy.loginfo(param_list)


if rospy.has_param(param_name_2_delete):
    rospy.loginfo('[ROSWay] Parameter exist')
else:
    rospy.loginfo('[ROSWay] Parameter not exist')
    

if rospy.has_param(param_name_2_delete):
    rospy.delete_param(param_name_2_delete)
    

if rospy.has_param(param_name_2_delete):
    rospy.loginfo('[ROSWay] Parameter exist')
else:
    rospy.loginfo('[ROSWay] Parameter not exist')
