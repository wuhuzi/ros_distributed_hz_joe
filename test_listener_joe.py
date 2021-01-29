#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


pub = rospy.Publisher('test2publish', String, queue_size=10)

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    rospy.sleep(3)
    pub.publish('test2publish')
    rospy.loginfo("json_str test2publish")

def test_sequence_listener():
    rospy.init_node('test_sequence_listener', anonymous=True)
    rospy.Subscriber("entities", String, callback)
    rospy.spin()


if __name__ == '__main__':
    test_sequence_listener()