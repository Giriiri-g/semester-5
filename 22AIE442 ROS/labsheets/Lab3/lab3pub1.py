#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def Publisher():
    rospy.init_node('publisher1', anonymous=True)
    pub = rospy.Publisher('nogui', String, queue_size=10)
    rate = rospy.Rate(1)
    string = "Hello world test test test".strip()
    count = len(string.split())

    while not rospy.is_shutdown():
        pub.publish(f'Word Count: {count}')
        rate.sleep()

if __name__ == '__main__':
    try:
        Publisher()
    except rospy.ROSInterruptException:
        pass
