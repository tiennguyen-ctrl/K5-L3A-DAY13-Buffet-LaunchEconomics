# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm: Buffet · Lớp: L3A. Cột trạng thái: **Xong, có bằng chứng · Chưa · Giả lập**. Gate 2a chỉ duyệt kế hoạch pilot.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated] cả 4 loại, gấp 16,3× hoá đơn token + tool (274,7 đ/yêu cầu). Pilot noi_dia + hang_nang: 3.414 đ, cộng cố định 40 triệu/tháng = **4.599 đ (0,38×)** ở 45.000 yêu cầu/tháng; nếu khối lượng giảm một nửa **5.784 đ (0,48×)** [simulated]. Nguồn: `bang_chi_phi.md` A2, A4 | Giả lập | Kế toán trưởng |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2 → **+51,8%** · xem lại ×2 → **+40,7%** · lương +25% → **+23,1%**; giá token ×2 chỉ +5,6% [simulated]. Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống. Nguồn: `bang_chi_phi.md` B1–B3 | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống (cộng 222 yêu cầu nhân viên làm thay): **5.865 đ/yêu cầu = 0,49×** của 12.000 đ [simulated]. Loại quoc_te (1,88×, thành công 27,3%) và doi_tac (0,85×, điều khoản riêng) khỏi pilot [simulated]. Nguồn: `bang_chi_phi.md` A3, B3 | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, dùng, an toàn | Chạy thử không đối chứng: đóng trong 24 giờ, không mở lại 7 ngày **82,83%** · bỏ qua gợi ý **27,12%** · mở lại 7 ngày **4,25%** (3,97% trong phạm vi) [simulated]. Đề xuất thêm: **tỉ lệ yêu cầu đủ điều kiện mà nhân viên mở trợ lý** và **tỉ lệ hoàn sai số tiền trong mẫu tuần**. Đã đặc tả 14 event có `trace_id`, chưa triển khai logging. Nguồn: `chi_so.md` E1 | Giả lập | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và khắc phục | Hai bộ nhãn độc lập trùng **20/20**, có bản gốc của từng người trong `nhan_doc_lap/`. Khắc phục 5 ca đủ 5 loại, mỗi dòng có event, ngưỡng, tần suất và vai trò phụ trách. Ưu tiên ca 20 (hoàn trùng), ca 7 (báo thành công khi sổ cái lỗi). Nguồn: `bang_loi.md` | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên, **20 + 20 cụm**, noi_dia + hang_nang; nhắm chênh **6 điểm** (859 yêu cầu hiệu dụng/nhóm). Nếu tác động thật chỉ 5 điểm thì **power ≈ 0,64**. Bốn luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ: hoàn trùng dừng trong 30 phút; mở lại chỉ tính cohort đủ theo dõi 7 ngày. Chờ xác nhận điều kiện triển khai. Nguồn: `pilot_plan.yaml` | Chưa | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại ×2 → **+51,8%** · xem lại 100% **0,98×** (1,03× nếu làm lại 15,3 phút), gần như không tiết kiệm · khối lượng còn một nửa → cố định **+2.370 đ/việc** [simulated]. Dấu hiệu, hành động và người phụ trách: `chi_so.md` E2 | Giả lập | Kế toán trưởng |

| Điều kiện trước khi bắt đầu pilot | Người phụ trách | Ngày kiểm tra |
| --- | --- | --- |
| Kiểm thử khoá chống trùng và đối soát sổ cái (ca 20, ca 7): 0 ca hoàn trùng, 0 thông báo thành công khi ghi sổ lỗi | Kỹ sư trưởng agent | 2026-12-04 |
| Ký chấp nhận chênh 6 điểm (power 0,64 nếu thật là 5 điểm); đủ 20 + 20 nhân viên, mỗi người ≥ 299 yêu cầu | Giám đốc vận hành | 2026-12-04 |
| Bật đủ 14 event có `trace_id` theo E1; sau tuần 1 thay phút xem lại, làm lại simulated bằng phút đo thật, tính lại chi phí | PM trợ lý hoàn phí | 2026-12-14 |
| Có kế hoạch giảm xem lại theo bậc: giảm khi sửa + bỏ < 15%, mỗi lần ≤ 5 phút; xem lại 100% = 0,98× [simulated] | Trưởng nhóm CSKH | 2026-12-21 |

**Đề xuất: Go có điều kiện** — chỉ pilot noi_dia + hang_nang (0,38× đã cộng cố định [simulated]), không mở quoc_te và doi_tac. Còn ba số bất lợi: xem lại 100% chỉ còn 0,98× [simulated]; power 0,64 nếu tác động thật là 5 điểm; mở lại 7 ngày đã 3,97% trong phạm vi. Điều kiện, người phụ trách và ngày kiểm tra ở bảng trên. Ngày quyết định sau pilot: 2027-01-08.
