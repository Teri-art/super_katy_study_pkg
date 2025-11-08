#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray

rospy.init_node('Polynominal_node')

pub = rospy.Publisher('summing_polynomials', Int32MultiArray, queue_size=10)

def polynm(msg):
    arr = msg.data
    arr2 = [0, 0, 0]
    for i in range(3):
        pwr = 3 - i  # степени: 3, 2, 1
        arr2[i] = arr[i] ** pwr
    msg.data = arr2
    rospy.loginfo(arr2)
    pub.publish(msg)

rospy.Subscriber('request_topic', Int32MultiArray, polynm, queue_size=10)
rospy.spin()
