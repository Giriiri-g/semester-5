#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String, Float32

def Lefty():
    key3 = rospy.Publisher('key3', String, queue_size=10)
    key2 = rospy.Publisher('key2', Float32, queue_size=10)
    rospy.init_node('Left', anonymous=True)
    rate = rospy.Rate(2) # 2 hz
    key_3 = "string"
    key_2 = 2.2
    while not rospy.is_shutdown():
        rospy.loginfo("Node 2")
        key3.publish(key_3)
        key2.publish(key_2)
        rate.sleep()

if __name__ == '__main__':
    try:
        Lefty()
    except rospy.ROSInterruptException:
        pass

