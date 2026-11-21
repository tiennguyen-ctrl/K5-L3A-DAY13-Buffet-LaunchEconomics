# Báo cáo cá nhân — Phan Nhật Trường (2A202603459)

## 1. Thông tin thành viên

- **Họ tên** Phan Nhật Trường
- **MSSV** 2A202603459
- **Email** Truong02052004@gmail.com
- **Nhóm và lớp** Buffet, L3A
- **Vai trò** Kiểm số A và B trước giờ giải lao, viết code D1 và E1 sau giờ giải lao.

## 2. Phần việc phụ trách

- Đối chiếu chi phí xem lại ở A2 và kiểm ảnh hưởng của các kịch bản tăng gấp đôi, giảm một nửa ở B1.
- Tính năm câu về cỡ mẫu D1, tỉ lệ mở lại trong 7 ngày và điền thông số cỡ mẫu vào `pilot_plan.yaml`.
- Tính ba chỉ số E1 từ dữ liệu chạy thử và điền kết quả vào `chi_so.md`. [Phân công nhóm](../../PHAN_CONG.md)

## 3. Đóng góp cụ thể

### Kiểm số A2 và B1

- **A2.** Tổng 890 phút xem lại từ cột `phut_xem_lai_simulated` nhân với 2.000 đ/phút cho **1.780.000 đ [simulated]**, khớp kết quả chương trình.
- **B1.** Khi giữ nguyên số việc thành công, gấp đôi một khoản chi làm tổng chi phí tăng đúng bằng khoản đó. Giảm một nửa khoản chi làm tổng giảm một nửa mức tăng, tính trước khi làm tròn. Giá token cho kết quả **+5,6% và −2,8%**. Chi phí xem lại cho kết quả **+40,7% và −20,3%** [simulated]. [Bảng chi phí và mục Kiểm số](bang_chi_phi.md#kiểm-số)

### D1 · Tính cỡ mẫu pilot

| Câu | Kết quả |
| --- | --- |
| a · Chia theo yêu cầu | Với baseline 70%, mục tiêu 75%, alpha 5% và power 80%, cần **1.251 yêu cầu mỗi nhóm**. |
| b · Chia theo nhân viên, 75 yêu cầu mỗi người | Hệ số thiết kế **2,48**. Cần **3.103 yêu cầu và 42 nhân viên mỗi nhóm**, tức 84 người trong khi chỉ có 40. |
| c · Chia 20 nhân viên mỗi nhóm | Cỡ mẫu hiệu dụng dưới **1.000 yêu cầu mỗi nhóm**. |
| d · Chia 6 depot mỗi nhóm | Cỡ mẫu hiệu dụng dưới **300 yêu cầu mỗi nhóm**. |
| e · Phát hiện chênh lệch 6 điểm phần trăm | Cần **859 yêu cầu hiệu dụng mỗi nhóm**. Với 20 nhân viên mỗi nhóm và ít nhất **299 yêu cầu mỗi người**, hệ số thiết kế là **6,96**. |

Với phương án chia theo nhân viên, nếu chênh lệch thực tế chỉ 5 điểm phần trăm thì power khoảng **64%**. Tỉ lệ mở lại trong 7 ngày trên dữ liệu giả lập là **4,25%** (51/1.200) toàn bộ và **3,97%** (39/982) trong phạm vi nội địa và hàng nặng. [Kế hoạch pilot](pilot_plan.yaml)

### E1 · Ba chỉ số chạy thử

| Chỉ số | Kết quả trên dữ liệu giả lập |
| --- | ---: |
| Đóng trong 24 giờ và không mở lại trong 7 ngày | **82,83%** (994/1.200) |
| Bỏ hoặc sửa gợi ý trong số yêu cầu đã xem lại | **27,12%** (48/177) |
| Mở lại trong 7 ngày | **4,25%** (51/1.200) |

Đây là các tỉ lệ quan sát trong đợt chạy thử giả lập. Thiết kế pilot có nhóm đối chứng để đánh giá tác động của trợ lý. [Bảng chỉ số](chi_so.md#e1--đặc-tả-chỉ-số)

## 4. Bằng chứng

- Commit `8fec924` chứa hai phần tính toán trong `src/lab13.py` và kết quả ghi vào `pilot_plan.yaml`, `chi_so.md`. [Commit D1/E1](https://github.com/tiennguyen-ctrl/K5-L3A-DAY13-Buffet-LaunchEconomics/commit/8fec9246cee26c2492d61cfd6d6b325decec0bc7)
- Chạy `python -X utf8 lab13.py` trong `src/`. Cả ba phép thử A1 đều đạt và chương trình in các kết quả D1, E1 như trên. [Mã tính toán](../../src/lab13.py)

## 5. Công cụ AI đã dùng

Dùng Codex để hỗ trợ viết mã D1/E1, kiểm tra đầu ra và soạn báo cáo từ các thay đổi có trong Git. Việc kiểm tra gồm chạy lại chương trình, đếm riêng tử số và mẫu số của E1 từ `logix_requests.csv`, rồi kiểm tra ranh giới cỡ mẫu bằng công thức `20m / (1 + (m − 1) × 0,02)`. Với 298 yêu cầu mỗi người, cỡ mẫu hiệu dụng khoảng 858,79. Với 299 yêu cầu, cỡ mẫu hiệu dụng khoảng 859,20 và đạt ngưỡng 859.

## 6. Tự đánh giá

Các kết quả tính từ dữ liệu chạy thử có thể tái lập từ mã và CSV. Điểm cần làm rõ khi trình bày là với 20 nhân viên mỗi nhóm, cỡ mẫu hiệu dụng vẫn dưới 1.000 dù tăng số yêu cầu trên mỗi người. Phương án phát hiện chênh lệch 6 điểm phần trăm chỉ khả thi nếu thu đủ ít nhất 299 yêu cầu mỗi nhân viên.
