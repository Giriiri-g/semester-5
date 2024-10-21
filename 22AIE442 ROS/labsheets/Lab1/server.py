#!/usr/bin/env python3
import rospy
from ros_service.srv import TwoInts, TwoIntsResponse

def handle_add_two_ints(req):
    return TwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_server')
    s = rospy.Service('add_two_ints', TwoInts, handle_add_two_ints)
    rospy.loginfo("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()