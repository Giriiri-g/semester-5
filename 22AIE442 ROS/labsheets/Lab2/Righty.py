#!/usr/bin/env python3
import rospy
from std_msgs.msg import String, Int16

def callback1(data):
    rospy.loginfo("Node 1 " + "Read %s", data.data)

def callback2(data):
    rospy.loginfo("Node 1 " + "Read %d", data.data)
    
def Righty():
    rospy.init_node('Node 1', anonymous=True)
    rospy.Subscriber("key3", String, callback1)
    rospy.Subscriber("key1", Int16, callback2)
    rospy.spin()

if __name__ == '__main__':
    Righty()
