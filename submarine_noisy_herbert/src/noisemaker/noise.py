#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Vector3
from std_msgs.msg import String
def start(name):
    rospy.init_node('python_sub_noisy_herbert', anonymous=True) # node is called 'python_simple_sub_simulator'

    pub = rospy.Publisher('python_submarine_logger', String, queue_size=10)
    happy_message = "100,100,200,3.14159,78.9,11.7,11.7,11.7||asjdhamsjdu ak jdjkshdkjasjdqg CRYING ANIMALS STUFFED PUFFIN CAKE"

    rate = rospy.Rate(50) # 50 lovely happy messages per second
    while not rospy.is_shutdown():
        pub.publish(happy_message)
        rate.sleep()
