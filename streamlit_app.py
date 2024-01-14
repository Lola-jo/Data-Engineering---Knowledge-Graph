import streamlit as st
from military_qa import MilitaryGraph
# 在你的主程序中使用新的 GraphGenerator 类

class StreamlitMilitaryGraph:
    def __init__(self):
        self.military_graph = MilitaryGraph()

    def parse_question(self, user_question):
        return self.military_graph.question_parser(user_question)

    def answer_question(self, parsed_question):
        results = self.military_graph.search_answer(parsed_question)
        if not results:
            return "对不起，目前暂时还无法回答此类问题..."
        else:
            result_strings = ["共找到%s个答案， 下面是具体明细：" % len(results)]
            for result in results:
                result_strings.append(result)
            return result_strings

    def qa_main(self, question):
        parser_dict = self.military_graph.question_parser(question)
        return self.answer_question(parser_dict)

    def display_weapon_image(self, weapon_name):
        weapon_image_path = query_mongo_image(weapon_name)
        if weapon_image_path:
            st.image(weapon_image_path, caption='武器图像', use_column_width=True)
        else:
            st.write('未找到该武器的图像')

def main():
    st.title('军事知识图谱问答')

    # 替换下面的地址为你的Neo4j可视化工具的地址
    neo4j_visualization_url = "http://43.156.52.96:7474/browser/"

    # 创建超链接
    link_text = "点击这里去查看图数据"
    link = f"[{link_text}]({neo4j_visualization_url})"
    st.markdown(link)

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
        results = streamlit_military_graph.qa_main(user_question)
        for result in results:
            st.write(result)
        st.write("解析后的问题：", parsed_question)

if __name__ == '__main__':
    main()