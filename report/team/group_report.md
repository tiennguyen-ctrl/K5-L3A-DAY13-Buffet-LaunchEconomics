# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm:
- Lớp:
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

...

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

...

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

...

## 5. Khó khăn và cách xử lý

- **Chạy `lab13.py` trên Windows báo `UnicodeEncodeError`** vì terminal không in được tiếng Việt. Xử lý: đặt `PYTHONUTF8=1` trước khi chạy; code không phải sửa.
- **So với 12.000 đ dễ ra kết luận quá lạc quan.** 4.472 đ chỉ chia cho việc trợ lý làm xong. Nhóm dùng chi phí cả hệ thống (cộng 222 yêu cầu nhân viên làm thay): 5.865 đ = 0,49×, không viết 0,37× [simulated].
- **Ngưỡng luật dừng an toàn.** Mở lại 7 ngày hiện tại đã 3,97% trong phạm vi, nên ngưỡng tuyệt đối 3% sẽ dừng pilot ngay tuần đầu. Nhóm đặt ngưỡng so với đối chứng (+2 điểm) kèm trần tuyệt đối 6%.
- **Không đủ người cho mức chênh 5 điểm** (cần 84 nhân viên, chỉ có 40). Nhóm chọn chia theo nhân viên 20 + 20 cụm, nhắm chênh 6 điểm, và nêu rõ power 0,64 nếu tác động thật chỉ 5 điểm.
- **Gắn nhãn độc lập.** Hai người gắn nhãn ghi vào bản riêng, chỉ chép vào `bang_loi.md` sau khi cả hai xong; đồng thuận 20/20, không sửa bộ độc lập sau khi so.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- **Phút xem lại và làm lại là số giả lập.** Chi phí, độ nhạy và rủi ro kinh tế đều phụ thuộc hai cột `_simulated`; cần thay bằng phút đo thật từ `staff_review_decision`, `staff_rework_completed` sau tuần 1 pilot.
- **Đợt chạy thử không có nhóm đối chứng.** 82,83% · 27,12% · 4,25% chỉ mô tả đợt chạy thử, chưa nói được tác động của trợ lý.
- **Power thấp ở mức 5 điểm** (0,64). Nếu tác động thật nhỏ, pilot dễ không kết luận được; cải thiện bằng cách thêm nhân viên hoặc kéo dài thời gian để tăng số yêu cầu mỗi người.
- **Xem lại 100% gần như không tiết kiệm** (0,98×, 1,03× nếu làm lại 15,3 phút) [simulated]. Cần kế hoạch giảm xem lại theo bậc, mỗi lần xem lại ≤ 5 phút.
- **Đồng thuận nhãn 100%** có thể do hai người dùng chung định nghĩa từ tài liệu; lần sau nên thử thêm một người gắn nhãn thứ ba hoặc các ca mơ hồ hơn để kiểm tra độ vững của quy tắc.

## 8. Tài liệu tham khảo

- Đề bài và hướng dẫn: `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `docs/du_lieu_va_cong_thuc.md`.
- Slide bài giảng: `docs/Ngay13_Slide_Launch_Economics.pdf`.
- Google PAIR, *People + AI Guidebook*, chương Errors + Graceful Failure (năm loại lỗi dùng ở nhiệm vụ C).
- statsmodels, `NormalIndPower` (tính power ở nhiệm vụ D).
- Dữ liệu giả lập: `src/logix_runs.csv`, `src/logix_requests.csv`.
