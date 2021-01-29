#!/usr/bin/env python3
# encoding: utf-8
import rospy
from std_msgs.msg import String
import json
json_str = "teste"
def talker_entity():
    pub = rospy.Publisher('entities', String, queue_size=10)
    rospy.init_node('talker_entity', anonymous=True)
    pub.publish(json_str)
    rospy.loginfo("json_str had send..")



if __name__ == '__main__':
    try:
        talker_entity()
    except rospy.ROSInterruptException:
        pass