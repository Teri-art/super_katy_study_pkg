#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('even_numbers_publisher')
pub = rospy.Publisher('even_numbers', Int32, queue_size=10)
rate = rospy.Rate(10)
counter = 0

while not rospy.is_shutdown():
    pub.publish(counter)
    rospy.loginfo("Published: %d", counter)
    counter += 2
    rate.sleep()
