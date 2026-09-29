import streamlit as st

st.title("🎓 我的第一個 Streamlit 網頁")

st.write("歡迎來到 Streamlit！")

name = st.text_input("請輸入姓名")

department = st.selectbox(
    "請選擇科系",
    ["資訊管理系", "資訊工程系", "其他"]
)

score = st.slider(
    "今天的課程滿意度",
    1, 5, 3
)

if st.button("送出"):
    if name == "":
        st.warning("請先輸入姓名")
    else:
        st.success("資料送出成功！")
        st.write("姓名：", name)
        st.write("科系：", department)
        st.write("滿意度：", score)