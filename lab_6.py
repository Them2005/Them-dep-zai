


import streamlit as st
import re



def clean_non_alphabetic(text):
    text = re.sub(r"[,.?!@#$%^&*()]", "", text)
    return text

def clean(text):
    text = text.lower()
    text = clean_non_alphabetic(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def tokenize(text):
    return text.split(' ')

def count_word(words):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Dữ liệu huấn luyện mẫu
train_spam = """Nhanh tay nhận ngay khuyến mãi cực lớn! Hôm nay duy nhất, giảm giá tới 70% cho hàng ngàn sản phẩm hot nhất thị trường. Cơ hội chỉ đến một lần, đừng bỏ lỡ! Truy cập ngay http://khuyenmai-sieuso.vn để đặt hàng với giá siêu sốc. Số lượng có hạn, ai nhanh tay người đó được!"""

train_not_spam = """Chào bạn, mình gửi thông báo về cuộc họp nhóm vào 9h sáng ngày mai tại phòng họp B2. Nội dung họp gồm: cập nhật tiến độ dự án, phân chia công việc tuần tới và thống nhất kế hoạch báo cáo. Bạn vui lòng chuẩn bị phần trình bày cá nhân và đến đúng giờ. Cảm ơn và hẹn gặp lại!"""

# Huấn luyện
clean_spam = clean(train_spam)
spam_words = tokenize(clean_spam)
total_spam_words = len(spam_words)
spam_freq = count_word(spam_words)

clean_not_spam = clean(train_not_spam)
not_spam_words = tokenize(clean_not_spam)
total_not_spam_words = len(not_spam_words)
not_spam_freq = count_word(not_spam_words)

# Từ vựng
vocab = set(spam_words + not_spam_words)
total_vocab = len(vocab)



def predict(text):
    text = clean(text)
    words = tokenize(text)
    prob_spam = 0.5
    prob_not_spam = 0.5

    for word in words:
    
        p_spam = (spam_freq.get(word, 0) + 1) / (total_spam_words + total_vocab)
        p_not_spam = (not_spam_freq.get(word, 0) + 1) / (total_not_spam_words + total_vocab)

        prob_spam *= p_spam
        prob_not_spam *= p_not_spam

    if prob_spam >= prob_not_spam:
        return ' Spam'
    else:
        return 'Not Spam'



st.title("Bộ lọc Spam và Not Spam")

input_text = st.text_area("Nhập nội dung email bạn muốn kiểm tra:", height=150)

if st.button("Dự đoán"):
    if input_text.strip() == "":
        st.warning("Vui lòng nhập nội dung.")
    else:
        result = predict(input_text)
        st.subheader("Kết quả:")
        st.success(result if "Not" in result else result)
