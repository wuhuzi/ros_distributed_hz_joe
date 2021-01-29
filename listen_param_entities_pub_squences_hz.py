#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import json
'''

{
    "response_code":"200",
    "MaxNumber":"7",
    "data":{
        "sequences":[
            {
                "skills":"init",
                "primitives":"回",
                "target_lable":"N",
                "target_pose":"N",
                "target_angle":"N",
                "target_high":"N"
            },
            {
                "skills":"抓取",
                "primitives":"趋",
                "target_lable":"螺母",
                "target_pose":"(0.86,0,0.545)",
                "target_angle":"(1.57, 1.57, 0)",
                "target_high":"N"
            },
            {
                "skills":"抓取",
                "primitives":"抓",
                "target_lable":"螺母",
                "target_pose":"N",
                "target_angle":"N",
                "target_high":"0.3"
            },
            {
                "skills":"抓取",
                "primitives":"提",
                "target_lable":"螺母",
                "target_pose":"N",
                "target_angle":"N",
                "target_high":"0.3"
            },
            {
                "skills":"对准",
                "primitives":"移",
                "target_lable":"螺栓",
                "target_pose":"(0.86,-0.20,0.645)",
                "target_angle":"(1.57, 1.57, 1.57)",
                "target_high":"N"
            },
            {
                "skills":"对准",
                "primitives":"下",
                "target_lable":"螺栓",
                "target_pose":"N",
                "target_angle":"N",
                "target_high":"N"
            },
            {
                "skills":"插入",
                "primitives":"放",
                "target_lable":"螺母",
                "target_pose":"N",
                "target_angle":"N",
                "target_high":"N"
            }
        ]
    }
}

'''
# 接收实体位姿封装值
def get_entity_param(data):

    # 打印转换好的dict ; str-->dict
    data = json.loads(data)
    # param_entity is list
    param_entity = data.get('param_entity')
    return param_entity



# 封装执行序列
sequences_data_encapsulate_json ="this is sequences"
def encapsulate_sequences(param_entity):
    # 获取带有封装参数的实体
    # param_entity = get_entity_param()
    print(param_entity)
    # 开始封装执行序列
    sequences_data_encapsulate = {}
    # 封装 response code
    sequences_data_encapsulate["response_code"] = "200"

    '''
    封装sequences
        1. 动作基元获取
        2. 动作基元参数封装
        3. 封装sequences
    '''
    # 1. 动作基元获取 assume primitives is lists name:primitives_list
    primitives_list = ["回", "趋", "抓", "提", "移", "下", "放"]
    sequences = []
    for primitive in primitives_list:
        primitive_dict = {}
        if(primitive == '回'):
            primitive_dict["skills"] = "init"
            primitive_dict["primitives"] = "回"
            primitive_dict["target_lable"] = 'N'
            primitive_dict["target_pose"] = 'N'
            primitive_dict["target_angle"] = 'N'
            primitive_dict["target_high"] = 'N'
            sequences.append(primitive_dict)

        if (primitive == '趋'):
            primitive_dict["skills"] = "抓取"
            primitive_dict["primitives"] = "趋"
            primitive_dict["target_lable"] = '螺母'
            primitive_dict["target_pose"] = '(0.86,0,0.545)'
            primitive_dict["target_angle"] = '(1.57, 1.57, 0)'
            primitive_dict["target_high"] = 'N'
            sequences.append(primitive_dict)

        if (primitive == '抓'):
            primitive_dict["skills"] = "抓取"
            primitive_dict["primitives"] = "抓"
            primitive_dict["target_lable"] = '螺母'
            primitive_dict["target_pose"] = 'N'
            primitive_dict["target_angle"] = 'N'
            primitive_dict["target_high"] = '0.3'
            sequences.append(primitive_dict)

        if (primitive == '提'):
            primitive_dict["skills"] = "抓取"
            primitive_dict["primitives"] = "提"
            primitive_dict["target_lable"] = '螺母'
            primitive_dict["target_pose"] = 'N'
            primitive_dict["target_angle"] = 'N'
            primitive_dict["target_high"] = '0.3'
            sequences.append(primitive_dict)

        if (primitive == '移'):
            primitive_dict["skills"] = "对准"
            primitive_dict["primitives"] = "移"
            primitive_dict["target_lable"] = '螺栓'
            primitive_dict["target_pose"] = '(0.86,-0.20,0.645)'
            primitive_dict["target_angle"] = '(1.57, 1.57, 1.57)'
            primitive_dict["target_high"] = 'N'
            sequences.append(primitive_dict)

        if (primitive == '下'):
            primitive_dict["skills"] = "对准"
            primitive_dict["primitives"] = "回"
            primitive_dict["target_lable"] = '螺栓'
            primitive_dict["target_pose"] = 'N'
            primitive_dict["target_angle"] = 'N'
            primitive_dict["target_high"] = 'N'
            sequences.append(primitive_dict)

        if (primitive == '放'):
            primitive_dict["skills"] = "插入"
            primitive_dict["primitives"] = "放"
            primitive_dict["target_lable"] = '螺母'
            primitive_dict["target_pose"] = 'N'
            primitive_dict["target_angle"] = 'N'
            primitive_dict["target_high"] = 'N'
            sequences.append(primitive_dict)

    # 统计sequences 的长度 并封装入json
    sequences_data_encapsulate["MaxNumber"] = len(sequences)
    # 封装sequences
    sequences_data_encapsulate["data"] = {"sequences": sequences}
    # 封装结果转为json
    sequences_data_encapsulate_json = json.dumps(sequences_data_encapsulate, ensure_ascii=False)

    return sequences_data_encapsulate_json

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    param_entity = get_entity_param(data.data)
    sequences_data_encapsulate_json = encapsulate_sequences(param_entity)
    rospy.loginfo(sequences_data_encapsulate_json)
    sequence_encapsulation_publish(sequences_data_encapsulate_json)
    rospy.loginfo("excute sequence_encapsulation_publish()")




def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/Vision/JsonTypeData/entities_processed", String, callback)
    rospy.spin()

# 全局变量
pub = rospy.Publisher('/Decider/JsonTypeData/Sequences', String, queue_size=10)
def sequence_encapsulation_publish(data):

    pub.publish(data)



def node_sub_pub():
    listener()





if __name__ == '__main__':
    node_sub_pub()
