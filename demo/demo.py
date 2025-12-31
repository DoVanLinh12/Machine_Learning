import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
from datetime import datetime

st.set_page_config(page_title="Bike Trip Predictor", layout="wide")
st.title("Dự báo thời gian di chuyển xe đạp công cộng")

# 1. Hàm load dữ liệu từ file pkl
@st.cache_resource
def load_data(name):
    filename = f"models/{name}_package.pkl"
    with open(filename, "rb") as f:
        return pickle.load(f)

# Sidebar để chọn mô hình
st.sidebar.header("Cài đặt")
model_option = st.sidebar.selectbox("Chọn mô hình", ["linear_regression", "decision_tree", "random_forest"])

try:
    pkg = load_data(model_option)
    model = pkg['model']
    features_in_model = pkg['features'] 
    start_map = pkg['start_map']
    end_map = pkg['end_map']
    valid_starts = pkg['valid_starts']
    valid_ends = pkg['valid_ends']
    coords = pkg['coords_dict']
    metrics = pkg['metrics']
except Exception as e:
    st.error(f"Lỗi tải mô hình: {e}")
    st.stop()

# 2. Hiển thị chỉ số đánh giá của mô hình
st.subheader(f"Chỉ số mô hình: {model_option.replace('_', ' ').upper()}")
m1, m2, m3 = st.columns(3)
m1.metric("MAE (Sai số giây)", f"{metrics['MAE']:.2f} s")
m2.metric("RMSE", f"{metrics['RMSE']:.2f} s")
m3.metric("R² Score", f"{metrics['R2']:.4f}")

st.divider()

# 3. Form nhập liệu
now = datetime.now()

st.subheader("Nhập thông tin chuyến đi")
with st.form("input_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        s_id = st.selectbox("Chọn trạm bắt đầu (ID)", valid_starts)
        s_lat = coords[s_id]['start_station_latitude']
        s_lon = coords[s_id]['start_station_longitude']
        st.write(f"Vĩ độ: `{s_lat}` | Kinh độ: `{s_lon}`")
        
        hr = st.slider("Giờ khởi hành", 0, 23, now.hour)

    with col2:
        e_id = st.selectbox("Chọn trạm kết thúc (ID)", valid_ends)
        e_lat = coords[e_id]['start_station_latitude']
        e_lon = coords[e_id]['start_station_longitude']
        st.write(f"Vĩ độ: `{e_lat}` | Kinh độ: `{e_lon}`")
        
        day = st.selectbox("Thứ trong tuần", range(7), index=now.weekday(),
                           format_func=lambda x: ["Thứ 2","Thứ 3","Thứ 4","Thứ 5","Thứ 6","Thứ 7","Chủ Nhật"][x])

    submitted = st.form_submit_button("Dự đoán thời gian")

if submitted:
    # Bước 1: Tra cứu giá trị Target Encoded
    s_enc = start_map[s_id]
    e_enc = end_map[e_id]
    
    # Bước 2: Tạo dictionary chứa các cột GỐC
    input_dict = {
        'start_station_latitude': s_lat,
        'start_station_longitude': s_lon,
        'end_station_latitude': e_lat,
        'end_station_longitude': e_lon,
        'start_time': hr,         
        'start_dayofweek': day, 
        'start_target_encoded': s_enc,
        'end_target_encoded': e_enc
    }
    
    # Bước 3: Tạo DataFrame và lọc/sắp xếp theo đúng thứ tự features của model
    try:
        input_df = pd.DataFrame([input_dict])
        for col in features_in_model:
            if col not in input_df.columns:
                input_df[col] = 0
        
        input_df = input_df[features_in_model]
        
        # Bước 4: Dự đoán
        pred_log = model.predict(input_df)
        final_seconds = np.expm1(pred_log)[0]
        
        # Hiển thị kết quả
        st.balloons()
        st.success(f"⏱️ Thời gian di chuyển dự kiến: **{final_seconds/60:.2f} phút** ({int(final_seconds)} giây)")
        
    except Exception as e:
        st.error(f"Lỗi khi dự báo: {e}")
        st.write("Các cột model yêu cầu:", features_in_model)