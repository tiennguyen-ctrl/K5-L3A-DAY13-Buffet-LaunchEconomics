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
- CP4: viết D2 (5 câu tách được tác động) và nháp 3 luật dừng (an toàn, chi phí, mức sử dụng) đủ NẾU – TRONG – THÌ – KHÔNG THÌ trong `pilot_plan.yaml`; ngưỡng an toàn so với đối chứng vì mở lại hiện tại đã 3,97%. Sang rà và tách luật hoàn trùng thành luật riêng, bản cuối có 4 luật dừng.
- CP5: 3 dòng rủi ro kinh tế trong `chi_so.md` E2.
- `group_report.md` mục 5 (khó khăn và cách xử lý), 7 (hạn chế và hướng cải thiện), 8 (tài liệu tham khảo).
- Giải quyết xung đột merge ở `ho_so_launch_v0.md` mục 4: giữ bản mới của Sang (14 event, trạng thái Giả lập vì chưa triển khai logging).

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- Commit `9c3659a` (daophuongcommit): `ho_so_launch_v0.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md` (E2).
- `report/team/ho_so_launch_v0.md` — 7 mục và dòng đề xuất.
- `report/team/bang_loi.md` — cột "Nhãn người 2", bảng khắc phục ca 14, 11.
- `report/team/pilot_plan.yaml` — D2, `identifiability`, `stop_rules`.
- `report/team/chi_so.md` — E2 rủi ro kinh tế.
- Commit `0869544` (daophuongcommit): `group_report.md` mục 5, 7, 8; hồ sơ mục 4; báo cáo cá nhân.
- Commit `72152d1` (daophuongcommit): merge với commit của Sang và Trường, giải quyết xung đột ở `ho_so_launch_v0.md`.
- `report/team/group_report.md` — mục 5, 7, 8.

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Claude Code (Claude Opus 5.5, trong VS Code):
  - Soạn nháp từ số nhóm đã tính (`bang_chi_phi.md`, `chi_so.md`, `pilot_plan.yaml`): 7 mục và dòng đề xuất của `ho_so_launch_v0.md`; D2 và 3 luật dừng; 3 dòng rủi ro kinh tế (E2); `group_report.md` mục 5, 7, 8; phần lớn báo cáo cá nhân này.
  - Chép hai bộ nhãn (của tôi và của Sang) vào `bang_loi.md`, đếm số ca trùng; gộp bảng khắc phục của hai người thành 5 ca, thống nhất tên vai trò phụ trách và thêm tên event.
- Cách tự kiểm: đối chiếu số trong hồ sơ với output `lab13.py` và `bang_chi_phi.md` (4.472 đ, 978 việc, 4.373.585 đ, khớp số đáp án trong tài liệu hướng dẫn); tự tính lại 5.865 đ = (4.373.585 + 222 × 12.000) / 1.200; kiểm `pilot_plan.yaml` bằng `yaml.safe_load` và không còn dấu `?`; rà từ cấm theo checklist SUBMISSION.md, không còn từ cấm trong `report/team`; nhờ Sang rà luật dừng và bảng khắc phục, Tiến chốt đề xuất.
- Không dùng AI để gắn nhãn 20 ca lỗi hay chấm nhóm bạn.

## 6. Tự đánh giá

- **Làm tốt:** giữ hồ sơ từ đầu buổi nên các mục được điền ngay khi có số, không dồn đến 16:36; hồ sơ nêu đủ ba con số bất lợi (0,98×, power 0,64, mở lại 3,97%) và ghi nhãn `simulated` ở mọi số giả lập; luật dừng an toàn đặt theo đối chứng thay vì ngưỡng tuyệt đối thấp hơn mức hiện tại.
- **Chưa tốt:** dựa nhiều vào AI để soạn nháp phần chữ, nên phải tự đọc lại và đối chiếu từng con số; bản nháp luật dừng ban đầu gộp hoàn trùng vào luật mở lại, Sang phải tách lại thành luật riêng.
- **Lần sau:** tự viết nháp trước rồi mới dùng AI để soát; thống nhất bộ tên vai trò phụ trách với cả nhóm ngay từ CP3 để không phải sửa lại ở nhiều file.
- **Tự chấm mức đóng góp:** khoảng 25%, tương đương các thành viên khác.
