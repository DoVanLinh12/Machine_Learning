# 🚲 Oslo City Bike Trip Duration Prediction

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/Task-Regression-green)]()

# Bài Toán
Bài toán đặt ra là xây dựng một hệ thống Machine Learning có khả năng: Dự đoán thời gian di chuyển khi sử dụng xe đạp tại thành phố Oslo dựa vào lịch sử của các chuyến đi trước đó 
Bài toán là dạng: Regression
# Mục tiêu
Dự đoán thời gian (s) di chuyển bằng xe đạp khi biết trạm xuất phát, trạm kết thúc, giờ khời hành, thứ trong tuần.
# Dataset
https://drive.google.com/file/d/1R8dizIJnlQVqzmpihocGayC-zqjUJ8wk/view?usp=sharing
# Thuộc tính dữ liệu
* **started_at**: Thời gian bắt đầu chuyến đi
* **ended_at**: Thời gian kết thúc chuyến đi
* **duration**: Thời gian di chuyển (s)
* **start_station_id**: Mã trạm bắt đầu
* **start_station_name**: Tên trạm bắt đầu
* **start_station_description**: Mô tả trạm bắt đầu
* **start_station_latitude**: Vĩ độ trạm đầu
* **start_station_longitude**: Kinh độ trạm đầu
* **end_station_id**: Mã trạm kết thúc
* **end_station_name**: Tên trạm kết thúc
* **end_station_description**: Mô tả trạm kết thúc
* **end_station_latitude**: Vĩ độ trạm cuối
* **end_station_longitude**: Kinh độ trạm cuối
# Pipline
Dataset → EDA → Clean → Encode → Train → Evaluate → Inference
# Mô hình
Linear Regression, Decision Tree, Random Forest
# Kết quả
| Mô hình | MAE (s) | RMSE (s) | $R^2$ Score |
| :--- | :---: | :---: | :---: |
| Linear Regression | 344.55 | 660.47 | 0.0620 |
| Decision Tree | 282.66 | 607.29 | 0.2069 |
| Random Forest | 239.74 | 573.21 | 0.2935 |
# Cách chạy
```bash
git clone https://github.com/DoVanLinh12/Machine_Learning.git
cd Machine_Learning
./run_project.cmd
```
# Tác giả
**Tác giả:** Đỗ Văn Linh | **MSV:** 12423040 | **Lớp:** 12423TN

