#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray, Int32

rospy.init_node('Request_node')

pub = rospy.Publisher('request_topic', Int32MultiArray, queue_size=10)

def request():
    msg = Int32MultiArray()
    input_arr = input("Пожалуйста, введите 3 числа: ").split()
    input_arr = [int(j) for j in input_arr]
    if len(input_arr) != 3:
        print('Нужно 3 числа !')
    else:
        msg.data = input_arr
        pub.publish(msg)
        rospy.loginfo("Отправлены числа: %s", input_arr)

def response(msg):
    print("Результат:", msg.data)
    rospy.signal_shutdown("Задание выполнено")

rospy.Subscriber('response_topic', Int32, response, queue_size=10)

try:
    request()
    rospy.spin()
except (rospy.ROSInterruptException, KeyboardInterrupt, TypeError):
    rospy.logerr('Exception catched')
except ValueError:
    print('Программа принимает только числа !')
