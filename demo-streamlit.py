import streamlit as st 
import datetime

st.title("Hello, DP 20201")


# Phan tinh tuoi 
st.header("Tinh tuoi")
nam_sinh = st.number_input(" Moi nhap nam sinh")

if nam_sinh:
    nam_hien_tai = 2025 # lay nam hien tai 
    tuoi = nam_hien_tai - nam_sinh

    st.write(f"Tuoi cua ban la: {tuoi} tuoi ")

# Tải file lên và đếm số lượng từ 
st.header("Ví dụ đếm từ trong file")
file_tai = st.file_uploader("Tải lên file văn bản")

if file_tai is not None:
    noi_dung = file_tai.read().decode("utf-8") # đọc nội dung flie 
    do_dai = len(noi_dung)
    st.write(f"File có {do_dai} từ")