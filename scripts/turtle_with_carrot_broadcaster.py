#!/usr/bin/env python3
import rospy
import tf
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose
import math

rospy.init_node('tf_turtle')

r = 0.0

def handle_carrot(msg, turtlename):
    global r
    if r >= 2 * math.pi:
        r = 0.0
    r += 0.1
    
    br = tf.TransformBroadcaster()
    br.sendTransform((1 * math.cos(math.pi * r), 1 * math.sin(math.pi * r), 0),
                     quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     "carrot",
                     turtlename)

if __name__ == '__main__':
    try:
        turtlename = rospy.get_param('~turtlename')  
        rospy.Subscriber('/%s/pose' % turtlename, Pose, handle_carrot, turtlename)
        rospy.spin()
    except Exception as e:
        rospy.logerr("Error: %s" % str(e))
