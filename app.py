import streamlit as st
import psycopg


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


# =========================
# Neon PostgreSQL 公告
# =========================

st.divider()
st.header("📢 最新公告")

try:
    conn = psycopg.connect(st.secrets["DATABASE_URL"])

    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, content, created_at
        FROM announcements_announcement
        ORDER BY created_at DESC
    """)

    announcements = cursor.fetchall()

    if announcements:
        for title, content, created_at in announcements:
            st.subheader(title)
            st.write(content)
            st.caption(f"發布時間：{created_at}")
    else:
        st.info("目前沒有公告")

    cursor.close()
    conn.close()

except Exception as e:
    st.error("目前無法讀取公告資料")
    st.exception(e)
