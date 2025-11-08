#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray, Int32

rospy.init_node('Summing_node')
pub_req = rospy.Publisher('response_topic', Int32, queue_size=10)

def summer(msg):
    s = sum(msg.data)
    msg2 = Int32()
    msg2.data = s
    pub_req.publish(msg2)
    rospy.loginfo("sum : %s", s)

rospy.Subscriber('summing_polynomials', Int32MultiArray, summer, queue_size=10)
rospy.spin()
