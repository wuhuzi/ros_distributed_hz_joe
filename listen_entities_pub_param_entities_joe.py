#!/usr/bin/env python3
import json
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

# encapsulate entities with param
param_entities_json = "this is param entities" # 定义publish json
def encapsulate_entities(entities,first_pose,second_pose):
    # define data eccapsulate param entity name
    param_entities_data = {}
    param_entities_data['response_code'] = 200
    # define data about param_entity
    param_entities_list = []
    # 组装param_entity_list todo: this part need to refactor by function method.
    param_entities_dict = {}
    rospy.loginfo(entities)
    rospy.loginfo(len(entities))
    rospy.loginfo(entities[0])
    param_entities_dict["target_lable"] = entities[0]
    param_entities_dict["target_pose"] = first_pose
    param_entities_dict["target_angle"] = 0
    param_entities_list.append(param_entities_dict)

    param_entities_dict["target_lable"] = entities[len(entities)-1]
    param_entities_dict["target_pose"] = second_pose
    param_entities_dict["target_angle"] = 0
    param_entities_list.append(param_entities_dict)

    # 封装数据
    param_entities_data['param_entity'] = param_entities_list
    param_entities_json = json.dumps(param_entities_data, ensure_ascii=False)
    return param_entities_json

# 全局变量
pub = rospy.Publisher('/Decider/JsonTypeData/ParamEntities', String, queue_size=10)
#  publish entities with param
def pub_param_entities(entities):
    param_entities_json = encapsulate_entities(entities,first_pose='',second_pose='')
    pub.publish(param_entities_json)
    rospy.loginfo(param_entities_json)


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    # excute pub entities with param
    pub_param_entities(data.data)
    rospy.loginfo("excute pub entities")


def listen_entities():
    rospy.init_node('listen_entities_pub_param_entities', anonymous=True)
    rospy.Subscriber("/Decider/JsonTypeData/Entities", String, callback)
    rospy.spin()


if __name__ == '__main__':
    listen_entities()