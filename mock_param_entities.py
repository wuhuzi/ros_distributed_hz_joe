#!/usr/bin/env python3
import jieba
import logging
import rospy
from std_msgs.msg import String

json_str = '''
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
# publish entities
def mock_param_entities():
    pub = rospy.Publisher('param_entities', String, queue_size=10)
    rospy.init_node('mock_param_entities', anonymous=True)
    pub.publish(json_str)
    rospy.loginfo(json_str)




if __name__ == '__main__':
    try:
        mock_param_entities()
    except rospy.ROSInterruptException:
        pass