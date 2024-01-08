# photo_show.py

import streamlit as st
# 在photo_show.py文件中创建MilitaryGraph实例并调用query_mongo_image方法
# 在photo_show.py文件中创建MilitaryGraph实例并调用query_mongo_image方法
from military_qa import MilitaryGraph

def main():
    st.title('武器图片展示')

    # 创建MilitaryGraph实例
    military_graph = MilitaryGraph()

    # 获取用户输入的武器名称
    weapon_name = st.text_input("请输入武器名称")

    if st.button('显示图片'):
        # 调用MilitaryGraph实例的query_mongo_image方法获取武器图片URL
        image_url = military_graph.query_mongo_image(weapon_name)

        # 在Streamlit应用程序中显示图片
        if image_url:
            st.image(image_url, caption='武器图片', use_column_width=True)
            st.write(f"武器名称: {weapon_name}")  # 打印图像的URL
            st.write(f"图像路径: {image_url}")  # 打印图像的URL
        else:
            st.write("未找到该武器的图片")
            st.write(f"武器名称: {weapon_name}")  # 打印图像的URL

if __name__ == "__main__":
    main()