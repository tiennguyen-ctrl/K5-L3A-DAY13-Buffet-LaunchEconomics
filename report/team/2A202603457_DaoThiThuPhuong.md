# Báo cáo cá nhân — DaoThiThuPhuong-2A202603457

## 1. Thông tin thành viên

- Họ tên: Đào Thị Thu Phương
- MSSV: 2A202603457
- Email: phuongdtt1824@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 2 kiêm giữ hồ sơ (không viết code)

## 2. Phần việc phụ trách

- Giữ hồ sơ `report/team/ho_so_launch_v0.md` từ đầu buổi: điền 7 mục, trạng thái, người phụ trách, dòng đề xuất cuối.
- CP3: gắn nhãn độc lập 20 ca lỗi (người gắn nhãn 2), cùng Sang so đồng thuận, viết quy tắc phân biệt, điền 2 ca trong bảng khắc phục.
- CP4: trả lời D2 (tách được tác động), nháp luật dừng trong `pilot_plan.yaml`.
- CP5: viết rủi ro kinh tế trong `chi_so.md`.
- Duyệt chéo: cùng Sang điền `phieu_cham.md`, ghi câu hỏi của hội đồng.
- `group_report.md` mục 5–8.

## 3. Đóng góp cụ thể

- Hồ sơ launch v0 (`ho_so_launch_v0.md`): điền đủ 7 mục, mỗi mục có con số chính, trạng thái, một vai trò phụ trách. Mục 1: 4.472 đ; phạm vi noi_dia + hang_nang cộng cố định 4.599 đ = 0,38×. Mục 3: chi phí cả hệ thống 5.865 đ = 0,49×. Mục 2: làm lại +51,8% · xem lại +40,7% · lương +23,1% [simulated].
- Dòng đề xuất **Go có điều kiện** với 4 điều kiện (người phụ trách, ngày kiểm tra), nêu rõ ba con số bất lợi: xem lại 100% = 0,98×, power 0,64, mở lại 3,97%.
- CP3: gắn nhãn độc lập 20 ca (người gắn nhãn 2); so với Sang đồng thuận 20/20; chọn 2 ca (14, 11) trong bảng khắc phục; tổng hợp `bang_loi.md`.
- CP4: viết D2 (5 câu tách được tác động) và 3 luật dừng (an toàn, chi phí, mức sử dụng) đủ NẾU – TRONG – THÌ – KHÔNG THÌ trong `pilot_plan.yaml`; ngưỡng an toàn so với đối chứng vì mở lại hiện tại đã 3,97%.
- CP5: 3 dòng rủi ro kinh tế trong `chi_so.md` E2.
- ... (bổ sung: phiếu chấm, group_report mục 5–8)

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- Commit `9c3659a` (daophuongcommit): `ho_so_launch_v0.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md` (E2).
- `report/team/ho_so_launch_v0.md` — 7 mục và dòng đề xuất.
- `report/team/bang_loi.md` — cột "Nhãn người 2", bảng khắc phục ca 14, 11.
- `report/team/pilot_plan.yaml` — D2, `identifiability`, `stop_rules`.
- `report/team/chi_so.md` — E2 rủi ro kinh tế.
- ... (bổ sung commit hồ sơ mục 4 và phiếu chấm, group_report)

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Claude Code: đọc tài liệu đề và `PHAN_CONG.md` để xác định phần việc và thứ tự chờ; cài môi trường (`.venv`, `pip install -r src/requirements.txt`) và chạy `src/lab13.py`; điền mục 1, 3 của hồ sơ từ số đã có trong `bang_chi_phi.md`.
- Cách tự kiểm: đối chiếu số trong hồ sơ với output `lab13.py` và `bang_chi_phi.md` (4.472 đ, 978 việc, 4.373.585 đ, khớp số đáp án trong tài liệu hướng dẫn); tự tính lại 5.865 đ = (4.373.585 + 222 × 12.000) / 1.200.
- Không dùng AI để gắn nhãn 20 ca lỗi hay chấm nhóm bạn.

## 6. Tự đánh giá

...
