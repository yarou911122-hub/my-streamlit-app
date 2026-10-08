import streamlit as st
st.set_page_config(page_title="個人介紹網站", layout="wide")
st.title("個人介紹網站")
st.write("歡迎來到我的個人網站")
a,b=st.columns([1,2])
with a:
    st.info("👩‍🎓 資訊工程系學生")
with b:
    st.subheader("關於我")
    st.write("我喜歡程式設計、攝影和閱讀。")
st.subheader("我的技能")
st.write("Python｜HTML｜CSS")
st.subheader("聯絡方式")
st.write("example@example.com")
