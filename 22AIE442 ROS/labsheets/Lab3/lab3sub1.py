#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(f"I received: {data.data}")

def subscriber():
    rospy.init_node('subscriber1', anonymous=True)
    rospy.Subscriber('nogui', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException:
        pass
