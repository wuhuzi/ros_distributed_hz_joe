#!/usr/bin/env python3
# encoding: utf-8
import rospy
from std_msgs.msg import String
import json
josn_str = '''

{
    "response_code":200,
    "param_entity":[
        {
            "target_lable":"螺母",
            "target_pose":"(x,y,z)",
            "target_angle":"θ"
        },
        {
            "target_lable":"螺栓",
            "target_pose":"(x,y,z)",
            "target_angle":"θ"
        }
    ]
}

'''
def talker_entity():
    pub = rospy.Publisher('/Decider/JsonTypeData/ParamEntities', String, queue_size=10)
    rospy.init_node('talker_entity', anonymous=True)
    pub.publish(josn_str)
    rospy.loginfo("json_str had send..")



if __name__ == '__main__':
    try:
        talker_entity()
    except rospy.ROSInterruptException:
        pass