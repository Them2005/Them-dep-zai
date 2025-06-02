import streamlit as st 

st.header("Đếm từ trong file:")

file_tai = st.file_uploader("Tải lên file văn bản:")

if file_tai is not None: 
    noi_dung = file_tai.read().decode('utf-8')  
    noi_dung = noi_dung.replace(',', '').replace('.', '')
    danh_sach_tu = noi_dung.split()
    do_dai = len(danh_sach_tu) 

    st.write(f"File có {do_dai} từ.")

    tan_suat = {}
    
    for tu in danh_sach_tu:
        if tu in tan_suat:
            tan_suat[tu] += 1 
        else:
            tan_suat[tu] = 1

    st.write("Tần suất các từ:", tan_suat)  

    van_ban = ''
    for tu, so_luong in tan_suat.items():
        van_ban += f'{tu}: {so_luong}\n' 

    # Tải file về 
    st.download_button(
        label="Tải file về",
        data=van_ban,  
        file_name="File_tai_ve.txt",
        mime="text/plain" 
    )

##SS 2 
st.header("Hiển thị file tần suất")

tan_suat = st.file_uploader("Chọn file tần suất")

if tan_suat is not None:
    noi_dung = tan_suat.read().decode("utf-8")
    tan_suat_tu = {}

    for dong in noi_dung.strip().split("\n"):
        if ":" in dong:
            parts = dong.split(":", 1)
            if len(parts) == 2:
                tu = parts[0].strip()
                so_luong = parts[1].replace(":", "").strip()
            
                if so_luong.isdigit():
                    tan_suat_tu[tu] = int(so_luong)

    st.subheader("Tần suất từ")
    st.write(tan_suat_tu)
