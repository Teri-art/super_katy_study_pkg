#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def overflow_callback(msg):
    rospy.loginfo("overflow 100")

rospy.init_node('overflow_listener')
rospy.Subscriber('overflow_notification', Int32, overflow_callback)

rospy.spin()
