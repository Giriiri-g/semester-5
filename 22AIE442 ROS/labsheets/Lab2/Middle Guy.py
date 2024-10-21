#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import Int16, Float32

def callback(data):
    rospy.loginfo("Node 3 " + "Read %f", data.data)

def Middle():
    key1 = rospy.Publisher('chatter', Int16, queue_size=10)
    rospy.init_node('counter', anonymous=True)
    rate = rospy.Rate(2) # 2 hz
    key_1 = 111
    while not rospy.is_shutdown():
        rospy.loginfo("Node 3")
        rospy.Subscriber("key2", Float32, callback)
        key1.publish(key_1)
        rate.sleep()

if __name__ == '__main__':
    try:
        Middle()
    except rospy.ROSInterruptException:
        pass

