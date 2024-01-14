import streamlit as st

st.title("Neo4j 数据展示")

# 替换下面的地址为你的Neo4j可视化工具的地址
neo4j_visualization_url = "http://43.156.52.96:7474/browser/"

# 创建超链接
link_text = "点击这里去查看图数据"
link = f"[{link_text}]({neo4j_visualization_url})"
st.markdown(link)
