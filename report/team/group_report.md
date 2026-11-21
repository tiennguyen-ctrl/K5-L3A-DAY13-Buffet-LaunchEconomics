# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Buffet
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí của LogiX-VN (dữ liệu giả lập) để trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào. Theo `TEAM.md` và `PHAN_CONG.md`, Tiến viết code A, B rồi kiểm số; Trường kiểm số rồi viết code D, E; Sang và Phương phụ trách gắn nhãn lỗi, Phương giữ hồ sơ. Quy trình yêu cầu gắn nhãn độc lập và kiểm số trước khi ghi "khớp"; bằng chứng gắn nhãn gốc còn chờ đối chiếu.

## 3. Giải pháp

- **A (chi phí mỗi việc thành công):** `src/lab13.py` (hàm `mo_hinh`) tính từ trace; tử số cộng mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `thanh_cong`. Chi tiết: [bang_chi_phi.md](bang_chi_phi.md) (A1–A4).
- **B (độ nhạy):** gọi lại `mo_hinh` cho 9 kịch bản, một cặp, giới hạn 1/2/3 lần chạy và xem lại 100%. Chi tiết: [bang_chi_phi.md](bang_chi_phi.md) (B1–B4).
- **C (bảng lỗi):** [bang_loi.md](bang_loi.md) có hai cột nhãn cho 20 ca và bảng khắc phục năm ca đủ năm loại; mỗi ca có event, ngưỡng, tần suất và một vai trò phụ trách. Hai cột hiện trùng 20/20; chờ đối chiếu bản gốc để xác nhận quy trình độc lập.
- **D (pilot):** [pilot_plan.yaml](pilot_plan.yaml) đặc tả chia ngẫu nhiên 20 nhân viên mỗi nhóm, ít nhất 299 yêu cầu/người để nhắm chênh 6 điểm phần trăm. Bốn luật dừng bao gồm hoàn trùng dừng trong 30 phút, mở lại 7 ngày, chi phí và mức sử dụng; điều kiện triển khai còn chờ xác nhận.
- **E (chỉ số, rủi ro, hồ sơ):** [chi_so.md](chi_so.md) có ba chỉ số tính thử, hai chỉ số đề xuất, 14 event và ba rủi ro kinh tế. [ho_so_launch_v0.md](ho_so_launch_v0.md) tổng hợp bảy mục và đề xuất có điều kiện; event mới là đặc tả cho pilot.

## 4. Kết quả

- Chi phí mỗi việc thành công: **4.472 đ** [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ); 978 việc thành công. So với nhân viên tự làm (cả hệ thống, gồm phần chuyển nhân viên): 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated].
- Theo loại: noi_dia 0,22×, hang_nang 0,69×, quoc_te 1,88×, doi_tac 0,85× [simulated]. quoc_te và doi_tac không đưa vào phạm vi pilot.
- Ba yếu tố nhạy nhất [simulated]: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%). Giá token chỉ +5,6%.
- Xem lại 100% (noi_dia + hang_nang): 0,98× (1,03× nếu làm lại 15,3 phút/ca) [simulated], gần như không tiết kiệm được gì. Giới hạn chạy 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ [simulated]).
- Cỡ mẫu pilot: chia theo yêu cầu cần 1.251/nhóm, nhưng chia theo nhân viên (20 + 20) chỉ đủ cho mức chênh 6 điểm (power khoảng 0,64 nếu tác động thật là 5 điểm).
- **Đề xuất của nhóm: Go có điều kiện** cho noi_dia + hang_nang, chi phí cộng cố định 4.599 đ/việc thành công = 0,38× của 12.000 đ [simulated]. Trước pilot cần kiểm thử chống hoàn trùng và báo thành công sai, xác nhận nhân sự/lưu lượng cho thiết kế chênh 6 điểm, bật event và chốt kế hoạch giảm xem lại. Người phụ trách, ngày kiểm tra và ngày quyết định 2027-01-08 ghi trong [hồ sơ launch](ho_so_launch_v0.md).
- **Duyệt chéo: Chưa có kết quả.** [Phiếu chấm](phieu_cham.md) đang chờ phân công và hồ sơ nhóm bạn; điểm, quyết định và phản hồi hội đồng dành cho nhóm mình sẽ được bổ sung theo bằng chứng thực tế.

## 5. Khó khăn và cách xử lý

- **Chạy `lab13.py` trên Windows báo `UnicodeEncodeError`** vì terminal không in được tiếng Việt. Xử lý: đặt `PYTHONUTF8=1` trước khi chạy; code không phải sửa.
- **So với 12.000 đ dễ ra kết luận quá lạc quan.** 4.472 đ chỉ chia cho việc trợ lý làm xong. Nhóm dùng chi phí cả hệ thống (cộng 222 yêu cầu nhân viên làm thay): 5.865 đ = 0,49×, không viết 0,37× [simulated].
- **Ngưỡng luật dừng an toàn.** Mở lại 7 ngày hiện tại đã 3,97% trong phạm vi, nên ngưỡng tuyệt đối 3% sẽ dừng pilot ngay tuần đầu. Nhóm đặt ngưỡng so với đối chứng (+2 điểm) kèm trần tuyệt đối 6%.
- **Không đủ người cho mức chênh 5 điểm** (cần 84 nhân viên, chỉ có 40). Nhóm chọn chia theo nhân viên 20 + 20 cụm, nhắm chênh 6 điểm, và nêu rõ power 0,64 nếu tác động thật chỉ 5 điểm.
- **Bằng chứng gắn nhãn độc lập.** Hai cột trong `bang_loi.md` hiện trùng 20/20. Sang và Phương cần đối chiếu, dẫn lại hai bản gốc được hoàn thành trước khi so nhãn; giữ nguyên bản gốc sau khi đối chiếu.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- **Phút xem lại và làm lại là số giả lập.** Chi phí, độ nhạy và rủi ro kinh tế đều phụ thuộc hai cột `_simulated`; cần thay bằng phút đo thật từ `staff_review_decision`, `staff_rework_completed` sau tuần 1 pilot.
- **Đợt chạy thử không có nhóm đối chứng.** 82,83% · 27,12% · 4,25% chỉ mô tả đợt chạy thử, chưa nói được tác động của trợ lý.
- **Power thấp ở mức 5 điểm** (0,64). Với 20 nhân viên/nhóm và ICC = 0,02, cỡ mẫu hiệu dụng là 20m / [1 + (m − 1) × 0,02] < 20 / 0,02 = 1.000, thấp hơn mức cần 1.251/nhóm. Kéo dài thời gian chỉ tăng m, không vượt trần này; cần thêm nhân viên/cụm độc lập nếu giữ mục tiêu 5 điểm. Nguồn: D1 trong [pilot_plan.yaml](pilot_plan.yaml).
- **Xem lại 100% gần như không tiết kiệm** (0,98×, 1,03× nếu làm lại 15,3 phút) [simulated]. Cần kế hoạch giảm xem lại theo bậc, mỗi lần xem lại ≤ 5 phút.
- **Hai cột nhãn trùng 100%** chỉ cho biết mức nhất quán của bảng hiện có, chưa xác minh được quá trình làm độc lập. Cần lưu và đối chiếu hai bản gốc; có thể bổ sung người gắn nhãn thứ ba hoặc ca mơ hồ hơn để kiểm tra quy tắc.

## 8. Tài liệu tham khảo

- Đề bài và hướng dẫn: `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `docs/du_lieu_va_cong_thuc.md`.
- Slide bài giảng: `docs/Ngay13_Slide_Launch_Economics.pdf`.
- Google PAIR, *People + AI Guidebook*, chương Errors + Graceful Failure (năm loại lỗi dùng ở nhiệm vụ C).
- statsmodels, `NormalIndPower` (tính power ở nhiệm vụ D).
- Dữ liệu giả lập: `src/logix_runs.csv`, `src/logix_requests.csv`.
