#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def mock_entities():
    rospy.init_node('mock_entities', anonymous=True)
    rospy.Subscriber("entities", String, callback)
    rospy.spin()


if __name__ == '__main__':
    mock_entities()