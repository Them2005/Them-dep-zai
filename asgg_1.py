import streamlit as st
import re
import os


tai_file_stop_words = st.file_uploader("Tải lên stopwords.txt", type="txt")
file_uploader = st.file_uploader("Tải lên giao-duc.txt", type="txt")
file_uploader = st.file_uploader("Tải lên the_thao.txt", type="txt")
file_uploader = st.file_uploader("Tải lên kinh-te.txt", type="txt")
def classify(text):
    text = text.lower()
    text = re.sub(r'[.,–?:@#$%^&*()+=_`~!{}"\n]', ' ', text)
    text = text.replace('  ', ' ')
    ds_tu = text.split()

    # Loại bỏ stop words
    with open('stopwords.txt', mode='r', encoding='utf-8') as f:
        stop_words = [line.strip() for line in f]
    ds_tu = [tu for tu in ds_tu if tu not in stop_words]

    topics = ['giao-duc', 'kinh-te', 'the-thao']
    scores = {}

    for topic in topics:
        freq = {}
        file_freq = topic + '-f.txt'
        if os.path.exists(file_freq):
            with open(file_freq, mode='r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(':')
                    if len(parts) == 2:
                        tu, count = parts[0].strip(), int(parts[1])
                        freq[tu] = count

        score = sum(freq.get(tu, 0) for tu in ds_tu)
        scores[topic] = score

    if max(scores.values()) == 0:
        return "Không xác định"
    return max(scores, key=scores.get)


st.title("Xác định thể loại văn bản")

van_ban = st.text_area("Mời nhập văn bản:")

if van_ban:
    the_loai = classify(van_ban)
    st.write("Thể loại của văn bản là: ", the_loai)


topics = ['giao-duc', 'kinh-te', 'the-thao']

for topic in topics:  
    file_tho = topic + '.txt'  
    with open(file_tho, mode='r', encoding='utf-8') as f:
        noi_dung = f.read()

    noi_dung = noi_dung.lower()
    noi_dung = re.sub(r'[.,–?:@#$%^&*()+=_`~!{}"\n]', ' ', noi_dung)

    with open('stopwords.txt', mode='r', encoding='utf-8') as f:
        stop_words = [line.rstrip() for line in f]

    for word in stop_words:
        noi_dung = noi_dung.replace(' ' + word + ' ', ' ')

    noi_dung = noi_dung.replace('  ', ' ')
    ds_tu = noi_dung.split(' ')

    tan_suat = {}
    for tu in ds_tu:
        if tu:
            tan_suat[tu] = tan_suat.get(tu, 0) + 1 

    file_out = topic + '-f.txt'
    with open(file_out, mode='w', encoding='utf-8') as f:
        for tu, count in tan_suat.items():  
            f.write(f'{tu}:{count}\n')

