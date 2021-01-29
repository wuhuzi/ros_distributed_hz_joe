#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def test_sequence_listener():
    rospy.init_node('test_sequence_listener', anonymous=True)
    rospy.Subscriber("/Decider/JsonTypeData/Sequences", String, callback)
    rospy.spin()


if __name__ == '__main__':
    test_sequence_listener()