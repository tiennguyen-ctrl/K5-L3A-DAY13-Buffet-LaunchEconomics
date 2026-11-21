# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Buffet · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công trên cả 4 loại (978/1.200 việc; gấp 16,3× hoá đơn token + tool 274,7 đ/yêu cầu) [simulated]. Phạm vi pilot noi_dia + hang_nang: 3.414 đ, cộng cố định 40 triệu/tháng = **4.599 đ (0,38×)** ở 45.000 yêu cầu/tháng; **5.784 đ (0,48×)** nếu khối lượng giảm một nửa [simulated]. Nguồn: `bang_chi_phi.md` A2, A4 | Giả lập | Kế toán trưởng |
| 2 · Ba yếu tố nhạy nhất | Khi gấp đôi từng yếu tố: 1. số ca làm lại **+51,8%** (6.787 đ) · 2. tỉ lệ xem lại **+40,7%** (6.292 đ) · 3. lương nhân viên +25% → **+23,1%**; giá token gấp đôi chỉ +5,6% [simulated]. Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ). Nguồn: `bang_chi_phi.md` B1–B3 | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống (đã cộng 222 yêu cầu không thành công do nhân viên làm, 12.000 đ/việc): (4.373.585 + 222 × 12.000) / 1.200 = **5.865 đ/yêu cầu = 0,49×** của 12.000 đ [simulated]. Theo loại: quoc_te 22.515 đ = **1,88×** (thành công 27,3%), doi_tac 0,85× → loại khỏi phạm vi pilot [simulated] | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử (1.200 yêu cầu, không có đối chứng): chính **82,83%** (994/1.200) · bỏ qua gợi ý **27,12%** (48/177) · mở lại 7 ngày **4,25%** (51/1.200; 3,97% trong phạm vi). Đã đặc tả **14 event** có `trace_id`, thêm chỉ số nhân viên mở trợ lý và hoàn sai số tiền trong mẫu tuần; chưa triển khai logging. Nguồn: `chi_so.md` E1 | Giả lập | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Hai bộ nhãn độc lập 20 ca, đồng thuận **20/20 = 100%**: Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn hệ thống 4 · Ngầm 3 (ca 5, 12, 17). Bảng khắc phục 5 ca (14, 20, 16, 11, 05), mỗi loại một ca, phát hiện bằng event có ngưỡng và tần suất; ưu tiên sửa ca 20 (hoàn hai lần, thiếu khoá chống trùng) và ca 7 (báo thành công khi sổ cái lỗi) trước pilot. Nguồn: `bang_loi.md` | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên, **20 + 20 cụm**, phạm vi noi_dia + hang_nang; nhắm chênh **6 điểm** (859 yêu cầu hiệu dụng/nhóm, m ≥ 299 yêu cầu/người, DE 6,96). Con số bất lợi: nếu tác động thật chỉ 5 điểm thì **power ≈ 0,64**. Bốn luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ: hoàn trùng dừng trong **30 phút**, mở lại chỉ tính cohort đủ theo dõi 7 ngày, chi phí và mức sử dụng. Kế hoạch đã đặc tả; chờ xác nhận nhân sự, lưu lượng và điều kiện trước pilot. Nguồn: `pilot_plan.yaml` | Chưa | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Ba rủi ro đã tính [simulated]: làm lại gấp đôi **+51,8%** (6.787 đ) · xem lại 100% **0,98×** (1,03× nếu làm lại 15,3 phút) — gần như không tiết kiệm · khối lượng còn một nửa → cố định **+2.370 đ/việc** (0,48×). Mỗi rủi ro có dấu hiệu, hành động, người phụ trách trong `chi_so.md` E2 | Giả lập | Kế toán trưởng |

**Đề xuất: Go có điều kiện** — chạy pilot chỉ cho noi_dia + hang_nang (4.599 đ = 0,38× đã cộng cố định [simulated]), không mở quoc_te (1,88×) và doi_tac (0,85×). Không chọn Go vì ba con số bất lợi chưa xử lý: xem lại 100% thì chỉ còn 0,98× (gần như không tiết kiệm) [simulated]; power chỉ 0,64 nếu tác động thật là 5 điểm; mở lại 7 ngày đã 3,97% trong phạm vi. Ngày quyết định sau pilot: 2027-01-08.

| Điều kiện trước khi bắt đầu pilot | Người phụ trách | Ngày kiểm tra |
| --- | --- | --- |
| Sửa khoá chống trùng (`idempotency_key`) và đối soát sổ cái để trợ lý không báo thành công khi ghi sổ lỗi (ca 20, ca 7); chạy lại kiểm thử, 0 ca hoàn trùng | Kỹ sư trưởng agent | 2026-12-04 |
| Ký chấp nhận mức chênh 6 điểm thay vì 5, với power 0,64 nếu tác động thật chỉ 5 điểm; xác nhận đủ 20 + 20 nhân viên, mỗi người ≥ 299 yêu cầu | Giám đốc vận hành | 2026-12-04 |
| Bật đủ event có `trace_id` (tối thiểu `staff_review_decision`, `staff_rework_completed`, `refund_ledger_write`, `ticket_reopened`); sau tuần 1 thay phút xem lại, làm lại simulated bằng phút đo thật và tính lại chi phí mỗi việc thành công | PM trợ lý hoàn phí | 2026-12-14 |
| Có kế hoạch giảm xem lại theo bậc (giảm khi tỉ lệ sửa + bỏ < 15%, mỗi lần xem lại ≤ 5 phút), vì xem lại 100% = 0,98× (1,03× nếu làm lại 15,3 phút) [simulated] | Trưởng nhóm CSKH | 2026-12-21 |
