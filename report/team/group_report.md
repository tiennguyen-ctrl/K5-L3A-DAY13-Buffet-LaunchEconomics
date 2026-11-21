# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Buffet
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí của LogiX-VN (dữ liệu giả lập) để trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào. Nhóm chia vai theo `TEAM.md` và `PHAN_CONG.md`: Tiến viết code A, B rồi kiểm số; Trường kiểm số rồi viết code D, E; Sang và Phương gắn nhãn lỗi độc lập, Phương giữ hồ sơ. Mỗi bảng số đều có người kiểm độc lập trước khi ghi "khớp".

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- **A (chi phí mỗi việc thành công):** `src/lab13.py` (hàm `mo_hinh`) tính từ trace; tử số cộng mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `thanh_cong`. Chi tiết: [bang_chi_phi.md](bang_chi_phi.md) (A1–A4).
- **B (độ nhạy):** gọi lại `mo_hinh` cho 9 kịch bản, một cặp, giới hạn 1/2/3 lần chạy và xem lại 100%. Chi tiết: [bang_chi_phi.md](bang_chi_phi.md) (B1–B4).
- **C (bảng lỗi):** [bang_loi.md](bang_loi.md) — (Sang, Phương điền kết quả đồng thuận và bảng khắc phục).
- **D (pilot):** [pilot_plan.yaml](pilot_plan.yaml) — (Trường, Phương điền sau khi hoàn thành).
- **E (chỉ số, rủi ro, hồ sơ):** [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md) — (điền sau khi hoàn thành).

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

- Chi phí mỗi việc thành công: **4.472 đ** [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ); 978 việc thành công. So với nhân viên tự làm (cả hệ thống, gồm phần chuyển nhân viên): 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated].
- Theo loại: noi_dia 0,22×, hang_nang 0,69×, quoc_te 1,88×, doi_tac 0,85× [simulated]. quoc_te và doi_tac không đưa vào phạm vi pilot.
- Ba yếu tố nhạy nhất [simulated]: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%). Giá token chỉ +5,6%.
- Xem lại 100% (noi_dia + hang_nang): 0,98× (1,03× nếu làm lại 15,3 phút/ca) [simulated], gần như không tiết kiệm được gì. Giới hạn chạy 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ [simulated]).
- Cỡ mẫu pilot: chia theo yêu cầu cần 1.251/nhóm, nhưng chia theo nhân viên (20 + 20) chỉ đủ cho mức chênh 6 điểm (power khoảng 0,64 nếu tác động thật là 5 điểm).
- Đề xuất cuối và kết quả duyệt chéo: (điền sau khi hoàn thành `ho_so_launch_v0.md` và buổi duyệt chéo).

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
