#!/usr/bin/env python
# encoding: utf-8
import rospy
from std_msgs.msg import String
import json
josn_str = '''
{
    "response_code":200,
    "data":{
        "sequences":[
            {
                "skills":"抓取",
                "primitives":"趋",
                "target_lable":"螺母",
                "target_pose":"(x,y,z)",
                "target_angle":"θ"
            },
            {
                "skills":"抓取",
                "primitives":"抓",
                "target_lable":"螺母",
                "target_pose":"(x,y,z)",
                "target_angle":"θ"
            },
            {
                "skills":"抓取",
                "primitives":"提",
                "target_lable":"螺母",
                "target_pose":"(x,y,z)",
                "target_angle":"θ"
            },
            {
                "skills":"对准",
                "primitives":"移",
                "target_lable":"螺栓",
                "target_pose":"(x,y,z)",
                "target_angle":"θ"
            },
            {
                "skills":"插入",
                "primitives":"放",
                "target_lable":"螺母",
                "target_pose":"(x,y,z)",
                "target_angle":"θ"
            },
            {
                "skills":"init",
                "primitives":"回",
                "target_lable":"",
                "target_pose":"(x,y,z)",
                "target_angle":"θ"
            }
        ]
    }
}
'''
def talker_entity():
    pub = rospy.Publisher('entities', String, queue_size=10)
    rospy.init_node('talker_entity', anonymous=True)
    pub.publish(josn_str)
    rospy.loginfo("json_str had send..")



if __name__ == '__main__':
    try:
        talker_entity()
    except rospy.ROSInterruptException:
        pass