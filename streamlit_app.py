# streamlit_app.py

import streamlit as st
from military_qa import MilitaryGraph  # 导入你的MilitaryGraph类

class StreamlitMilitaryGraph:
    def __init__(self):
        self.military_graph = MilitaryGraph()

    def parse_question(self, user_question):
        return self.military_graph.question_parser(user_question)

    def answer_question(self, parsed_question):
        return self.military_graph.search_answer(parsed_question)  # 更新这里的调用方式

def main():
    st.title('军事知识图谱问答')  # 设置应用的标题

    # 展示问题提问方式
    st.write("问题提问方式：")
    question_types = [
        ["属性值问答", "单实体单属性问答", "神舟五号的长度是多少?"],
        ["属性值问答", "单实体多属性问答", "神舟五号的长度以及运载火箭是多少?"],
        ["属性值问答", "多实体单属性问答", "神舟五号以及神舟十号的长度是多少?"],
        ["属性值问答", "多实体多属性问答", "神舟五号的长度,运载火箭以及辽宁舰艇的航长分别为多少是多少?"],
        ["属性区间值筛选问答", "单属性区间问答", "最大飞行速度大于500公里的战斗机?"],
        ["属性区间值筛选问答", "单属性多区间问答", "服役时间在1950年之后2000年之前的轰炸机?"],
        ["属性区间值筛选问答", "多属性多区间问答", "服役时间在1950年之后2000年之前且最大航程大于5000公里的运输机?"],
        ["属性最值筛选", "单实体属性最值问答", "长度最长的宇宙飞船"]
    ]
    st.table(question_types)

    streamlit_military_graph = StreamlitMilitaryGraph()

    user_question = st.text_input("请输入你的问题：")

    if user_question:
        parsed_question = streamlit_military_graph.parse_question(user_question)
        answer = streamlit_military_graph.answer_question(parsed_question)
        st.write("回答：", answer)  # 先展示回答结果
        st.write("解析后的问题：", parsed_question)  # 再展示解析后的问题

if __name__ == '__main__':
    main()