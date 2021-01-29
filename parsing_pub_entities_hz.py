#!/usr/bin/env python3
import jieba
import logging
import json
import rospy
from std_msgs.msg import String
logger = logging.getLogger()
logger.setLevel('DEBUG')
def parse_order():
    try:
        # 输入用户/流水线任务指令 螺母装配螺栓
        # user_commands = input("input your order:")
        user_commands = "螺母装配螺栓"
        # 分词
        seg_list = list(jieba.cut(user_commands, cut_all=False))
        logging.debug('seg_list:' + str(seg_list))  # 精确模式
        # 获取first entity
        begin_entity = seg_list[0]
        logging.info('begin_entity:' + str(begin_entity))
        # 获取最后一个实体
        # todo: first entity using last entity. this entity needed by language context.
        final_entity = seg_list[len(seg_list) - 1]
        logging.info('final_entity:' + str(final_entity))
        return [begin_entity, final_entity]
    except Exception as  e:
        rospy.loginfo("parse order error")



# publish entities
def talker_entity():
    # 循环接受指令
    while not rospy.is_shutdown():
        pub = rospy.Publisher('/Vision/JsonTypeData/entities_unprocessed', String, queue_size=10)
        rospy.init_node('talker_entity', anonymous=True)
        # 获取实体列表
        entities = parse_order()

        param_entities_data = {}
        param_entities_data['response_code'] = 200
        # define data about param_entity
        param_entities_list = []
        for entity in entities:
            rospy.loginfo(entity)


            # 组装param_entity_list todo: this part need to refactor by function method.
            param_entities_dict = {}

            param_entities_dict["skills"] = "init"
            param_entities_dict["primitives"] = "回"
            param_entities_dict["target_lable"] = entity
            param_entities_dict["target_pose"] = '(x,y,z)'
            param_entities_dict["target_angle"] = '(x,y,z)'
            param_entities_dict["target_high"] = 'N'
            param_entities_list.append(param_entities_dict)

        # 封装数据
        param_entities_data['param_entity'] = param_entities_list
        param_entities_json = json.dumps(param_entities_data, ensure_ascii=False)

        # 发布实体列表用于封装
        pub.publish(param_entities_json)
        rospy.loginfo(param_entities_json)
        rospy.loginfo("waiting for next order")
        rospy.sleep(6)


if __name__ == '__main__':
    try:
        talker_entity()
    except rospy.ROSInterruptException:
        pass