#!/usr/bin/env python
import rospy
from datetime import datetime
import time

def time_node():
    rospy.init_node('time_node', anonymous=True)
    rate = rospy.Rate(0.2)  # 0.2 Hz = каждые 5 секунд
    
    rospy.loginfo("Time node started. Publishing time every 5 seconds...")
    
    while not rospy.is_shutdown():
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rospy.loginfo("Current time: %s", current_time)
        rate.sleep()

if __name__ == '__main__':
    try:
        time_node()
    except rospy.ROSInterruptException:
        pass
