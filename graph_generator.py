from military_qa import MilitaryGraph
import networkx as nx
import matplotlib.pyplot as plt
import jieba
import jieba.posseg as pseg


def extract_features(intro):
    # 使用jieba进行中文分词和词性标注
    words = pseg.lcut(intro)
    
    # 初始化特征量列表
    features = []
    
    # 提取国家、武器种类和设计者等信息
    country = ""
    weapon_type = ""
    designer = ""
    
    for word, flag in words:
        if flag == 'ns':  # ns为地名词性
            country = word
        elif flag == 'n':  # n为普通名词词性
            weapon_type = word
        elif flag == 'nr':  # nr为人名词性
            designer = word
    
    # 将提取的信息作为特征量添加到特征量列表中
    if country:
        features.append(country)
    if weapon_type:
        features.append(weapon_type)
    if designer:
        features.append(designer)
    
    return features

# 创建 MilitaryGraph 实例
military_graph = MilitaryGraph()

# 获取所有数据
all_data = military_graph.get_introduction()

# 创建一个空的无向图
G = nx.Graph()

# 提取每条数据的【简介】语句中的特征量，并构建知识图谱
for data in all_data:
    intro = data.get("简介", "")  # 获取简介语句
    features = extract_features(intro)  # 提取特征量的函数，需要根据实际情况编写
    for feature in features:
        G.add_node(feature, type="特征量")
        G.add_edge(data["名称"], feature, relation="包含")

# 绘制图形
pos = nx.spring_layout(G)  # 使用弹簧布局算法
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_weight='bold', font_size=10, font_family='SimHei', edge_color='gray')  # 绘制图形
plt.show()  # 显示图形