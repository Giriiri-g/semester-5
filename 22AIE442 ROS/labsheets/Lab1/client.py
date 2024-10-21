#!/usr/bin/env python3
import rospy
from ros_service.srv import TwoInts

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', TwoInts)
        resp1 = add_two_ints(x, y)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

if __name__ == "__main__":
    rospy.init_node('add_client')
    x = 5
    y = 3
    print("Requesting %d + %d" % (x, y))
    print("Sum: %d" % add_two_ints_client(x, y))